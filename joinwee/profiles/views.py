# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from userena.utils import generate_sha1, get_protocol, \
     get_datetime_now
from userena.mail import send_mail

from profiles.models import Profile, ConfirEmail
from .utils import string2py
from profiles.forms import NewSocialUserForm

@login_required
def manager_lesson(request, username):
    user = User.objects.get(username=username)
    if request.user == user:
        profile = user.profile
        lessons = user.weelesson_set.published()
        draft_lessons = user.weelesson_set.draft()
    else:
        raise Http404()

    return render_to_response('userena/manager_lesson.html',
                              {'lessons': lessons,
                               'draft_lessons': draft_lessons,
                               'profile': profile},
                              context_instance=RequestContext(request))

@login_required
def new_social_user(request):
    '''添加一个新的WEE用户'''
    ## TODO: 当一个已验证的用户访问时，应该出现一个404页面
    confirm = request.user.confiremail_set.all()
    _username = string2py(request.user.username)
    request.user.username = _username
    request.user.save()
    
    if request.user.email:
        if confirm:
            is_active = confirm[0].active
        else:
            is_active =True

        return render_to_response('userena/wee_signup.html',
                                  {'is_active': is_active},
                                  context_instance=RequestContext(request))       
            
    if request.method == 'POST':

        form = NewSocialUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user

            #user.username = _username
            user.set_password(cd['password1'])
            user.email = cd['email']
            salt, hash = generate_sha1(_username)

            cf = ConfirEmail(user=user,
                             email_confirmation_key=hash,
                             email_confirmation_key_created=get_datetime_now())
            cf.save() # 生成一个关于此用户的验证数据
            
            ctx = {
                
                'user': user,
                'email': user.email,
                'protocol': get_protocol(),
                'confirmation_key': hash,
                'site': Site.objects.get_current()}
            
            user.save() # 将信息写入到用户数据中

            subject = render_to_string('userena/emails/email_confir_subject.txt', ctx)
            subject = ''.join(subject.splitlines())

            message_html = None

            message = render_to_string('userena/emails/email_confir_message.txt', ctx)

            if user.email:
                send_mail(subject,
                          message,
                          message_html,
                          settings.DEFAULT_FROM_EMAIL,
                          [user.email])
                
            return HttpResponseRedirect('/')
    else:
        form = NewSocialUserForm()

    return render_to_response('userena/new-social-user.html',
                              {"form":form},
                              context_instance=RequestContext(request))

def email_confirm(request, c_key):
    '''创建新的邮件之后，接收验证'''
    
    is_active = True
    try:
        ce = ConfirEmail.objects.get(email_confirmation_key=c_key,
                                     active=False)
        ce.active = True
        ce.save()
    except ConfirEmail.DoesNotExist:
        is_active = False

    return render_to_response('userena/email_confirm_1.html',
                              {'is_active': is_active},
                              context_instance=RequestContext(request))

@login_required
def sns_link(request):
    ctx = {
        'last_login': request.session.get('social_auth_last_login_backend')
        }
    return render_to_response('userena/sns_link.html', ctx, RequestContext(request))

@login_required
def sns_redirect(request):
    return HttpResponseRedirect(reverse('userena.views.profile_detail', args=(request.user.username, )))


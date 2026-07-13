# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.crypto import get_random_string
import hashlib

from profiles.models import Profile, ConfirEmail
from .utils import string2py
from profiles.forms import NewSocialUserForm, BsEditProfileForm


def generate_sha1(string):
    salt = get_random_string(length=5)
    hash = hashlib.sha1((salt + string).encode('utf-8')).hexdigest()
    return salt, hash


def get_datetime_now():
    return timezone.now()


def get_protocol():
    return 'https' if settings.USE_HTTPS else 'http'


def profile_list(request):
    profiles = Profile.objects.select_related('user').all()
    return render(request, 'userena/profile_list.html', {'profile_list': profiles})

def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    return render(request, 'userena/profile_detail.html', {'profile': profile, 'user': user})

@login_required
def profile_edit(request, username):
    user = get_object_or_404(User, username=username)
    if request.user != user:
        raise Http404()
    profile = user.profile
    if request.method == 'POST':
        form = BsEditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userena_profile_edit', args=(username,)))
    else:
        form = BsEditProfileForm(instance=profile)
    return render(request, 'userena/profile_form.html', {'form': form, 'profile': profile, 'user': user})

@login_required
def manager_lesson(request, username):
    user = User.objects.get(username=username)
    if request.user == user:
        profile = user.profile
        lessons = user.weelesson_set.published()
        draft_lessons = user.weelesson_set.draft()
    else:
        raise Http404()

    return render(request, 'userena/manager_lesson.html',
                              {'lessons': lessons,
                               'draft_lessons': draft_lessons,
                               'profile': profile})

@login_required
def new_social_user(request):
    '''添加一个新的WEE用户'''
    confirm = request.user.confiremail_set.all()
    _username = string2py(request.user.username)
    request.user.username = _username
    request.user.save()
    
    if request.user.email:
        if confirm:
            is_active = confirm[0].active
        else:
            is_active = True

        return render(request, 'userena/wee_signup.html',
                                  {'is_active': is_active})       
            
    if request.method == 'POST':

        form = NewSocialUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user

            user.set_password(cd['password1'])
            user.email = cd['email']
            salt, hash = generate_sha1(_username)

            cf = ConfirEmail(user=user,
                             email_confirmation_key=hash,
                             email_confirmation_key_created=get_datetime_now())
            cf.save()
            
            ctx = {
                
                'user': user,
                'email': user.email,
                'protocol': get_protocol(),
                'confirmation_key': hash,
                'site': Site.objects.get_current()}
            
            user.save()

            subject = render_to_string('userena/emails/email_confir_subject.txt', ctx)
            subject = ''.join(subject.splitlines())

            message = render_to_string('userena/emails/email_confir_message.txt', ctx)

            if user.email:
                send_mail(subject,
                          message,
                          settings.DEFAULT_FROM_EMAIL,
                          [user.email])
                
            return HttpResponseRedirect('/')
    else:
        form = NewSocialUserForm()

    return render(request, 'userena/new-social-user.html',
                              {"form": form})

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

    return render(request, 'userena/email_confirm_1.html',
                              {'is_active': is_active})

@login_required
def sns_link(request):
    ctx = {
        'last_login': request.session.get('social_auth_last_login_backend')
        }
    return render(request, 'userena/sns_link.html', ctx)

@login_required
def sns_redirect(request):
    return HttpResponseRedirect(reverse('profile_edit', args=(request.user.username,)))

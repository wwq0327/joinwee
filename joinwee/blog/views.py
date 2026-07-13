# Create your views here.

# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from blog.models import Post

def index(request):
    posts = Post.objects.all()
    
    return render_to_response('blog/index.html',
                              {'posts': posts,
                               'last': posts[:10]
                               },
                              context_instance=RequestContext(request))

def post(request, slug):
    posts = Post.objects.all()
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/post.html',
                              {'post': post,
                               'last': posts[:10]
                               },
                              context_instance=RequestContext(request))

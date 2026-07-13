# Create your views here.

# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from blog.models import Post

def index(request):
    posts = Post.objects.all()

    return render(request, 'blog/index.html', {'posts': posts, 'last': posts[:10]})

def post(request, slug):
    posts = Post.objects.all()
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post, 'last': posts[:10]})

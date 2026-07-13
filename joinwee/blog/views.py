# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django import forms

from blog.models import Post, BlogComment


class CommentForm(forms.Form):
    content = forms.CharField(label=u'', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': '写下你的评论...'}))


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts, 'last': posts[:10]})

def post(request, slug):
    posts = Post.objects.all()
    p = get_object_or_404(Post, slug=slug)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            BlogComment.objects.create(
                post=p,
                user=request.user,
                content=form.cleaned_data['content']
            )
            return HttpResponseRedirect(p.get_absolute_url())
    else:
        form = CommentForm()

    comments = p.comments.all()
    return render(request, 'blog/post.html', {
        'post': p,
        'last': posts[:10],
        'comments': comments,
        'form': form,
    })

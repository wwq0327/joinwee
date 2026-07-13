from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.urls import reverse

from home.models import First
from home.forms import FirstForm
from weelesson.models import WEELesson
from weemeet.models import WEEMeet

def index(request):
    lessons = WEELesson.objects.filter(is_fine=True, is_draft=False)

    return render(request, 'home/index.html', {'lessons': lessons[:8]})

def succ(request):
    return render(request, 'home/succ.html')

def about(request):
    return render(request, 'home/about.html')



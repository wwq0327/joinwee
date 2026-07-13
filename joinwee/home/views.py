from django.shortcuts import render

from weelesson.models import WEELesson
from weemeet.models import WEEMeet

def index(request):
    lessons = WEELesson.objects.filter(is_fine=True, is_draft=False).select_related('creater')

    return render(request, 'home/index.html', {'lessons': lessons[:8]})

def succ(request):
    return render(request, 'home/succ.html')

def about(request):
    return render(request, 'home/about.html')



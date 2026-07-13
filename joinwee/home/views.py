from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from home.models import First
from home.forms import FirstForm
from weelesson.models import WEELesson
from weemeet.models import WEEMeet

def index(request):
    lessons = get_list_or_404(WEELesson, is_fine=True, is_draft=False)
    #meets = get_list_or_404(WEEMeet)

    return render_to_response('home/index.html',
            {'lessons': lessons[:8]},
            context_instance=RequestContext(request))

def succ(request):
    return render_to_response('home/succ.html',
            {},
            context_instance=RequestContext(request))

def about(request):
    return render_to_response('home/about.html',
            {},
            context_instance=RequestContext(request))



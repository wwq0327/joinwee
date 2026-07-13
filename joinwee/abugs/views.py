from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from home.models import First
from home.forms import FirstForm

def server_error(request):
    return render_to_response('500.html', RequestContext(request))

def page_not_found(request):
    return render_to_response('404.html', RequestContext(request))


def denied(request):
    if request.method == 'POST':
        form = FirstForm(request.POST)
        if form.is_valid():
            o = form.save(commit=False)
            o.save()
            return HttpResponseRedirect(reverse('home.views.succ'))
    else:
        form = FirstForm()

    return render_to_response('403.html', 
            {'form': form,},
            context_instance=RequestContext(request))




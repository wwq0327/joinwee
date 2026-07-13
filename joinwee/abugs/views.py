from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from home.models import First
from home.forms import FirstForm

def server_error(request):
    return render(request, '500.html')

def page_not_found(request, exception):
    return render(request, '404.html')

def denied(request, exception):
    if request.method == 'POST':
        form = FirstForm(request.POST)
        if form.is_valid():
            o = form.save(commit=False)
            o.save()
            return HttpResponseRedirect(reverse('home_succ'))
    else:
        form = FirstForm()

    return render(request, '403.html', {'form': form})

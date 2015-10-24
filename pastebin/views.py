from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from pastebin.models import Paste
from pastebin.forms import *
import hashlib, random

def paste_create(request):

    if request.method == 'POST':
        paste_form = PasteForm(request.POST)

        if paste_form.is_valid():
            paste = paste_form.save(commit=False)
            url_key = hashlib.md5(str(paste.pk) + str(random.randint(10000, 1000000))).hexdigest()[:10]
            paste.url_key = url_key
            paste.save()
            
            return HttpResponseRedirect(reverse('pastebin:view', args=[url_key]))

    else:
        paste_form = PasteForm()
        
    return render(request, 'pastebin/new_paste.html',{'paste_form' : paste_form})

def paste_get(request,key):

    if request.method == 'GET':
        paste = Paste.objects.get(url_key = key)
        
        return render(request, 'pastebin/view_paste.html', {'paste' : paste})

def paste_fork(request,key):
    
    paste_forked = Paste.objects.get(url_key = key)
    paste_form = PasteForm(instance=paste_forked)

    return render(request, 'pastebin/new_paste.html',{'paste_form' : paste_form})

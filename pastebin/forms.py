import datetime

from django import forms
from django.conf import settings

from pastebin.models import Paste

class PasteForm(forms.ModelForm):
    
    class Meta:
        model = Paste
        fields = ('title','text',)
         

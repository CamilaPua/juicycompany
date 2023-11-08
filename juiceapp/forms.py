from django import forms
from .models import Juice

class JuiceForm(forms.Form):
    juices = forms.ModelChoiceField(queryset=Juice.objects.all())
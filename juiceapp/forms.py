from django import forms
from juiceapp.models import Juice, User

class JuiceForm(forms.Form):
    juices = forms.ModelChoiceField(queryset=Juice.objects.all())

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)

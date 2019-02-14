from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('info', 'url')

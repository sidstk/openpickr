from django import forms
from django.contrib.auth.models import User

from .models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['name','comment','image']

class ImageLike(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['name','is_like']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
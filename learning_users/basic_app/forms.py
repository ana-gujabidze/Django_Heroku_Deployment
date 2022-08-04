from django import forms
from django.contrib.auth.models import User

from basic_app.models import UserProfileModelInfo


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileFormInfo(forms.ModelForm):
    class Meta():
        model = UserProfileModelInfo
        fields = ('profile_url', 'profile_image')

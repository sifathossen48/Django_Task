from django import forms
from django.contrib.auth.models import User

from website.models import Comment


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=32)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
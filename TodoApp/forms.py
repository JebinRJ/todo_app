from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from TodoApp.models import *

class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput(), max_length='8')
    password2 = forms.CharField(widget=forms.PasswordInput(), max_length='8')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Profile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class Create(forms.ModelForm):
    class Meta:
        model=CreateTodo
        fields=['todo','status']





from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', help_text='Limited to 150 symbols', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', help_text='Limited to 150 symbols',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()
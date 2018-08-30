from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label='login')
    password=forms.CharField(label='password', widget=forms.PasswordInput)
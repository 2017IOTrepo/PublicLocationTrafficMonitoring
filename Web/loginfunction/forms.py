# coding=utf-8

from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("您两次输入的密码不一致，请重试")
        return cd["password2"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


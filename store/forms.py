from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import User
from django.forms.utils import ErrorList
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])


class UserSignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'required': True}),
            'first_name': TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': EmailInput(attrs={'class': 'form-control', 'required': True}),
        }

    def clean(self):
        cleaned_data = super(UserSignUpForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        username = cleaned_data.get('username')

        return cleaned_data


class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name']

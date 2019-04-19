from django import forms

from django.contrib.auth.forms  import UserCreationForm

from Accounts.models import *


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", 'autocomplete':"nope", "placeholder":"Email address"}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={"class":"form-control", 'autocomplete':"new-password", "placeholder":"*************" }))


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2'
        }

    '''    widgets = {
            'email' :forms.EmailInput(attrs={"id":"email", "class":"form-control", 'autocomplete':"nope", 'placeholder':"Email", 'required':'required'}),
            'first_name' :forms.TextInput(attrs={"id":"firstname", "class":"form-control", 'autocomplete':"nope", 'placeholder':"First Name", 'required':'required'}),
            'last_name' :forms.TextInput(attrs={"id":"lastname", "class":"form-control", 'autocomplete':"nope", 'placeholder':"Last Name", 'required':'required'}),
        }'''


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
        'industry','company_name','company_size','address','state','city','postcode','country','company_logo',
        )

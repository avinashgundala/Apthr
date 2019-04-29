from django import forms

from django.contrib.auth.forms  import UserCreationForm,AuthenticationForm

from Accounts.models import *


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", 'autocomplete':"nope", "placeholder":"Email address"}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={"class":"form-control", 'autocomplete':"new-password", "placeholder":"*************" }))


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2',
                    'agree'
        )

        widgets = {
            'email' :forms.EmailInput(attrs={"class":"form-control", 'autocomplete':"nope", 'placeholder':"Email", 'required':'required'}),
            'first_name' :forms.TextInput(attrs={"class":"form-control", 'autocomplete':"nope", 'placeholder':"First Name", 'required':'required'}),
            'last_name' :forms.TextInput(attrs={"class":"form-control", 'autocomplete':"nope", 'placeholder':"Last Name", 'required':'required'}),

        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
        'industry','company_name','city','postcode','country','company_logo','company_type','contact_no'
        )
        widgets ={
            'industry':forms.Select(attrs={'placeholder':'industry','class':'chosen'}),
            'company_name':forms.TextInput(attrs={'placeholder':'company name'}),
            #'company_size':forms.Select(attrs={"id":"",'placeholder':''}),
            'company_type':forms.Select(attrs={'placeholder':'company type','class':'chosen'}),
            #'address':forms.Textarea(attrs={"id":"",'placeholder':''}),
            #'state':forms.TextInput(attrs={"id":"",'placeholder':''}),
            'city':forms.TextInput(attrs={'placeholder':'city'}),
            'postcode':forms.TextInput(attrs={'placeholder':'postcode'}),
            'country':forms.Select(attrs={'placeholder':'country','class':'chosen'}),
            'company_logo':forms.FileInput(attrs={'placeholder':'company logo', 'onchange':'Validateimgupload(this)','class':'inputfile inputfile-1'}),
            'contact_no':forms.TextInput(attrs={'placeholder':'contact no'})

        }

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name','email','rating','subject','message')
        widgets = {
              'subject':forms.Select(attrs={'class':'chosen'}),
              'email':forms.EmailInput(attrs={'placeholder':'email'})
        }

class ActivationEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())


'''class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name','email','country_code','mobile','subject','message')'''

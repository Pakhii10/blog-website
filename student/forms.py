# from django import forms

# class blogform(forms.Form):
#     username=forms.CharField()
#     blog_title=forms.CharField()
#     blog_description=forms.CharField()
#     blog_video = forms.FileField()

# class login(forms.Form):
#     username=forms.CharField()
#     password=forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['firstname','lastname','contactdetail','email','username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class blogform(forms.Form):
   
    blog_title=forms.CharField()
    blog_description=forms.CharField()
    blog_video = forms.FileField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
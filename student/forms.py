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
from .models import UserLogin

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ['firstname','lastname','contactdetail','email','username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
class blogform(forms.Form):
    username=forms.CharField()
    blog_title=forms.CharField()
    blog_description=forms.CharField()
    blog_video = forms.FileField()

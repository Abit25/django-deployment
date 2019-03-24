from django import forms
from django.core import validators
from AppTwo.models import UserProfileInfo
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):

    username=forms.CharField(widget=forms.TextInput(
    attrs={"class":"input100" ,"name":"fn" ,"placeholder":"Username"
    }
    ))
    email=forms.EmailField(widget=forms.TextInput(
    attrs={"class":"input100" ,"name":"ln" ,"placeholder":"Email"
    }
    ))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100" ,"name":"eml" ,"placeholder":"Password"
    }))

    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    profile_pic=forms.ImageField(widget=forms.FileInput(
    attrs={"class":"input100" ,"name":"pp" ,"placeholder":"Profile Pic","required":False
    }
    ))
    portfolio_site=forms.URLField(widget=forms.TextInput(
    attrs={"class":"input100" ,"name":"ps" ,"placeholder":"Portfolio Site",'required':False
    }))

    class Meta:

        model=UserProfileInfo
        fields=("profile_pic","portfolio_site")

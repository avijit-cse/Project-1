from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from App_Login.models import Userprofile





class singup_from(UserCreationForm):
    email= forms.EmailField(label="Email Adress",required=True)

    class Meta:
        model=User
        fields=('username','email','password1','password2')

class userprofilechange(UserChangeForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password')




class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Userprofile
        fields = ['profile_pic']


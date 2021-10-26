from django import forms
from  Blog_main.models import  Comment,Blog


class Commentfrom(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comments',)

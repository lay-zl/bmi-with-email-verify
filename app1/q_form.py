from django import forms
from .models import CustomUser


class UpadteUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email']
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email'
        }
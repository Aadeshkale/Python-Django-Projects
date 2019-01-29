from django import forms
from myapp.models import Auser
class RegForm(forms.ModelForm,forms.Form):
    class Meta():
        model=Auser
        fields='__all__'
    userid=forms.CharField(max_length=20,
    label="Enter Your Username",
    widget=forms.TextInput(attrs={
        'class':'text-left form-control',
    })
    )
    password=forms.CharField(max_length=30,
    label="Enter Your Password",
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
    })
    )
    repassword=forms.CharField(max_length=30,
    label="Conform Your Password",
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
    })
    )

class LoginForm(forms.Form):
    userid=forms.CharField(max_length=20,
    label="Enter Your Username",
    widget=forms.TextInput(attrs={
        'class':'text-left form-control',
    })
    )
    password=forms.CharField(max_length=30,
    label="Enter Your Password",
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
    })
    )
class UserForm(forms.Form):
    userid=forms.CharField(max_length=20,
    label="Enter Your Username",
    widget=forms.TextInput(attrs={
        'class':'text-left form-control',
        'placeholder':'Enter userid',
    })
    )
    password=forms.CharField(max_length=30,
    label="Enter Your Password",
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Default password',
    })
    )

from django import forms
from formapp.models import Emp
class EmpFrom(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'
   

    name=forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Name',
        })
    )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Email',
        })
    )
    phone=forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Phone',          
        })
    )
    gen=[
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
        ]
    gender=forms.ChoiceField(choices=gen,
        widget=forms.RadioSelect(),
    )
    cty=[
        ('Aurangabad','Aurangabad'),
        ('Pune','Pune'),
        ('Hyderabad','Hyderabad'),
        ]
    city=forms.ChoiceField(choices=cty)


class Empupd(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'
        
    
    ids=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter emp id'
            }
        )
    ) 
    name=forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Name',
        })
    )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Email',
        })
    )
    phone=forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Phone',          
        })
    )
    gen=[
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
        ]
    gender=forms.ChoiceField(choices=gen,
        widget=forms.RadioSelect(),
    )
    cty=[
        ('Aurangabad','Aurangabad'),
        ('Pune','Pune'),
        ('Hyderabad','Hyderabad'),
        ]
    city=forms.ChoiceField(choices=cty)

class EmpDel(forms.ModelForm):
    class Meta:
        model=Emp   
        fields=['eid']
    ids=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter emp id'
            }
        )
    ) 
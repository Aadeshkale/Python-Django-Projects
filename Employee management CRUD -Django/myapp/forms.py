from django import forms
from myapp.models import Emp
class InsertForm(forms.ModelForm):
    class Meta():
        model=Emp
        fields="__all__"
    name=forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={
        'placeholder':'Enter Emp name',
        'class':'form-control',
    })
    )    
    email=forms.EmailField(max_length=50,
    widget=forms.EmailInput(attrs={
        'placeholder':'Enter Emp email',
        'class':'form-control',
    })
    )
    gen=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    gender=forms.ChoiceField(
    choices=gen,
    widget=forms.RadioSelect(attrs={
    })
    )
    gen=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    cou=[
        ('India','India'),
        ('Other','Other'),
    ]
    country=forms.ChoiceField(
    choices=cou,
    )

class UpdateForm(forms.Form):
    email=forms.EmailField(max_length=20,
    widget=forms.EmailInput(attrs={
        'placeholder':'Enter ur email',
        'class':'form-control',
    })
    )
    cou=[
        ('India','India'),
        ('Other','Other'),
    ]
    country=forms.ChoiceField(choices=cou,
        widget=forms.RadioSelect(),
    )

class DeleteForm(forms.Form):
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder':'Enter ur email to delete record',
            'class':'form-control',
        })
    )
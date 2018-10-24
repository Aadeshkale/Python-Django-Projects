from django import forms

class Send(forms.Form):
    name=forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter ur name',
    })
    )

    subject=forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Subject',
    })
    )

    comment=forms.CharField( #max_length=100,
    widget=forms.Textarea(attrs={ 
        'class':'form-control',
        'placeholder':'Enter ur comment',
    }))
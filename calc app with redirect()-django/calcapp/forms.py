from django import forms

class Cal(forms.Form):
    num1=forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder':'Enter ur First no'
        })
    )
    num2=forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder':'Enter ur Second no'
        })
    )
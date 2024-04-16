from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        widgets = {

            'product': forms.TextInput(attrs={'class':'form-control'}),
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'comments': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'stars': forms.Select(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control','type':'date'})
        }
        labels={
            'fname':'first_name',
            'lname':'last_name'
        }
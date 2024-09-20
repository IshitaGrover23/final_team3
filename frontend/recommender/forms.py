from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type symptoms such as itching, sleeping, aching etc'}))
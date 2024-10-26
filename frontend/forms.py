from django import forms
from forms import ModelForm


class Registration(forms.models.ModelForm):
    class Meta:
        fields = ['name', 'email', 'phone']
        model = 'registration'


""" class login():
 """    
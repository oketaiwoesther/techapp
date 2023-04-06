from django import forms

class PostForm(forms.Form):
    image = forms.FileField()
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'} ))
    discriptions = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder':'Enter description', 'class':'form-control'}),required=True)
    


#models.py from django.db import models

#forms.py from django import forms from .models import User





from django import forms
from .models import Services

class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        exclude = ('created_on' , 'updated_on',)

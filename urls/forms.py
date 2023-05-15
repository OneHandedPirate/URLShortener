from django import forms
from .models import Token

from .utils import create_short_url

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['original_url']
        widgets = {
            'original_url': forms.TextInput(attrs={'placeholder': 'Enter URL...',
                                                   'class': 'form-control my-3 mx-auto shadow',
                                                   'id': 'url-input',
                                                   'style': 'max-width:500px;'})
        }
        labels = {
            'original_url': ''
        }


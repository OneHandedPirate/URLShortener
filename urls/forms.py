from django import forms

from .models import Token
from .utils import check_short_url


class TokenForm(forms.ModelForm):
    """Form for creating a new token"""

    class Meta:
        model = Token
        fields = ['original_url']
        widgets = {
            'original_url': forms.TextInput(attrs={'placeholder': 'Enter URL...',
                                                   'class': 'form-control my-3 mx-auto shadow',
                                                   'id': 'url-input',
                                                   'style': 'max-width:600px;'})
        }
        labels = {
            'original_url': ''
        }

    def clean_original_url(self):
        original_url = self.cleaned_data['original_url']
        if check_short_url(original_url):
            raise forms.ValidationError('This link is already shortened')
        return original_url

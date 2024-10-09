from django import forms
from django.core.validators import EmailValidator

from django.utils.translation import gettext as _

class ContactForm(forms.Form):


    subject = forms.CharField(max_length=100, required=True, label=_("Objet"), widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(validators=[EmailValidator()], required=True, label="E-mail",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField( required=True,
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control'}))




# verification/forms.py
from django import forms
from verification_app.models import PhoneNumber

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['name','phone_number']

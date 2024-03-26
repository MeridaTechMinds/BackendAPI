from django import forms
from .models import PropertyModel,image_model

class PropertyForm(forms.ModelForm):
    class Meta:
        model = PropertyModel
        fields = "__all__"
       
    
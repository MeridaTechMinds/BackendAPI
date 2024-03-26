from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import*

class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class ReviewAdminForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.ReviewedBy:
            instance.ReviewedBy = self.current_user.username
        if commit:
            instance.save()
        return instance

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"  # Adjust fields as per your Review model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


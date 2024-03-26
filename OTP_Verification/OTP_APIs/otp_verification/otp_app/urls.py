# urls.py

from django.urls import path
from .views import verify_phone_number, verify_code

app_name = 'verification_app'

urlpatterns = [
    path('verifys/', verify_phone_number, name='verify_phone_number'),
    path('verify/<int:id>/', verify_code, name='verify_code'),
]

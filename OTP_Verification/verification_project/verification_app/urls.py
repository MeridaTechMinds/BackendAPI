from django.urls import path
from .views import verify_phone_number, verify_code,generate_qr_code

app_name = 'verification_app'

urlpatterns = [
    path('verify/', verify_phone_number, name='verify_phone_number'),
    path('verify/<int:phone_number_id>/', verify_code, name='verify_code'),
    path("qrcode",generate_qr_code),
    
]
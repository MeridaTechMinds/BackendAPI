from rest_framework import serializers

# serializers.py

from .models import PhoneNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id', 'name', 'phone_number',"verification_code",'is_verified', 'count_no', 'offer']

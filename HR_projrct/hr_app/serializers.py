from rest_framework import serializers
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields = '__all__'
        
# class ReviewSerializer(serializers.ModelSerializer):
#     user_name = RegistrationSerializer(many=True)
#     class Meta:
#         model = Review
#         fields = '__all__'

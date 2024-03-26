from rest_framework import serializers
from .models import *
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'

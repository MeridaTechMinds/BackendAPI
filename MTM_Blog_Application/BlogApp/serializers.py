from rest_framework import serializers
from .models import Blog, Points,Comments,contact,Apointment
from .models import *

class pointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = '__all__'
        
class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    points = pointSerializer(many=True)
    comments = commentSerializer(many=True)
    class Meta:
        model = Blog
        fields = '__all__'


class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        # fields = '__all__'
        fields=['first_name','last_name','company','interested','phone','email','message']

class ApointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apointment
        fields = '__all__'




from .models import Job_Portal,Details,job_points
        
class job_points_Serializer(serializers.ModelSerializer):
    class Meta:
        model = job_points
        fields = '__all__'


class jobserializers(serializers.ModelSerializer):
    points = job_points_Serializer(many=True)
    class Meta:
        model=Job_Portal
        fields="__all__"
        


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'

    # def to_representation(self, instance):
    #     self.fields['user'] = jobserializers(read_only=True)
    #     return super(DetailSerializer, self).to_representation(instance)

class subscribSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = '__all__'



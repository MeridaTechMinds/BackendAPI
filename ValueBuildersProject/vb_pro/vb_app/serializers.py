from rest_framework import serializers
from .models import *

class imageserializers(serializers.ModelSerializer):
    class Meta:
        model=image_model
        fields="__all__"
    


class property_serializer(serializers.ModelSerializer):
    images = imageserializers(many=True)
    class Meta:
        model=PropertyModel
        fields="__all__"

    # def create(self, validated_data):
    #     images_data = self.context.get('request').data.get('images', [])
    #     property_instance = PropertyModel.objects.create(**validated_data)
    #     for image_data in images_data:
    #         image_serializer = imageserializers(data=image_data)
    #         if image_serializer.is_valid():
    #             image_serializer.save(property=property_instance)
    #         else:
    #             # Handle serializer errors as per your requirements
    #             pass
    #     return property_instance

    def get_images(self, obj):
        request = self.context.get('request')
        images_queryset = obj.images.all()
        images_serializer = imageserializers(instance=images_queryset, many=True, context={'request': request})
        return images_serializer.data


class contact_serializer(serializers.ModelSerializer):
    class Meta:
        model=contact
        fields="__all__"
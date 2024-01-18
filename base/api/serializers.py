from rest_framework.serializers import ModelSerializer
from base.models import *



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'title', 'profile_picture', 'agency', 'is_agency_admin', 'request_status', 'contact_number', 'description']


class AgencySerializer(ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'




class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyFeaturesSerializer(ModelSerializer):
    class Meta:
        model = PropertyFeatures
        fields = '__all__'


class HouseImagesSerializer(ModelSerializer):
    class Meta:
        model = HouseImages
        fields = '__all__'

class HouseVideosSerializer(ModelSerializer):
    class Meta:
        model = HouseVideos
        fields = '__all__'

        
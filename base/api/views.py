from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import *
from .serializers import *
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from django.http import Http404
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import requests
import random
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'POST /api/add-a-house/',
        'POST /api/add-house-image/',
        'POST /api/delete-image/',
        'POST /api/delete-a-house/',
        'POST /api/get-houses/',
        'POST /api/get-a-houses/'
    ]

    return Response(routes)

@api_view(['GET'])
def getHouses(request):
    try:
        # Get all properties
        properties = Property.objects.all()

        # Serialize property data
        property_data = PropertySerializer(properties, many=True).data

        # Create a list to store all houses data
        all_houses_data = []

        # Iterate through each property to get related data
        for property_obj in properties:
            features_obj = PropertyFeatures.objects.filter(property=property_obj)
            house_imgages_obj = HouseImages.objects.filter(property=property_obj)
            house_videos_obj = HouseVideos.objects.filter(property=property_obj)
            user_obj = User.objects.get(id=property_obj.user.id)
            agency_obj = Agency.objects.get(id=user_obj.agency.id)

            property_feature_data = PropertyFeaturesSerializer(features_obj, many=True).data
            house_imgages_data = HouseImagesSerializer(house_imgages_obj, many=True).data
            house_videos_data = HouseVideosSerializer(house_videos_obj, many=True).data
            user_data = UserSerializer(user_obj, many=False).data
            agency_data = AgencySerializer(agency_obj, many=False).data

            user_data["agency"] = agency_data

            property_data_item = PropertySerializer(property_obj, many=False).data
            property_data_item["user"] = user_data

            house_data = {
                "Property": property_data_item,
                "PropertyFeatures": property_feature_data,
                "HouseImages": house_imgages_data,
                "HouseVideos": house_videos_data
            }

            all_houses_data.append(house_data)

        return Response({"houses": all_houses_data}, status=status.HTTP_200_OK)

    except Property.DoesNotExist:
        return Response({'error': 'No houses found'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getHouse(request, property_id):
    try:
        property_obj = Property.objects.get(id=property_id)
        features_obj = PropertyFeatures.objects.filter(property=property_obj)
        house_imgages_obj = HouseImages.objects.filter(property=property_obj)
        house_videos_obj = HouseVideos.objects.filter(property=property_obj)
        user_obj = User.objects.get(id=property_obj.user.id)
        agency_obj = Agency.objects.get(id=user_obj.agency.id)

        property_data = PropertySerializer(property_obj, many=False).data
        property_feature_data = PropertyFeaturesSerializer(features_obj, many=True).data
        house_imgages_data = HouseImagesSerializer(house_imgages_obj, many=True).data
        house_videos_data = HouseVideosSerializer(house_videos_obj, many=True).data
        user_data = UserSerializer(user_obj, many=False).data
        agency_data = AgencySerializer(agency_obj, many=False).data

        user_data["agency"] = agency_data

        property_data["user"] = user_data

        house_data = {
            "Property": property_data,
            "PropertyFeatures": property_feature_data,
            "HouseImages": house_imgages_data,
            "HouseVideos": house_videos_data

        }

        return Response({"house": house_data}, status=status.HTTP_200_OK)

    except Property.DoesNotExist:
        return Response({'error': 'Property not found'}, status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def addAHouse(request):
    resume = Resume.objects.get(tracking=tracking)
    affiliation = Affiliations.objects.get(resume=resume.pk)
    affiliation.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def addHouseImage(request):
    resume = Resume.objects.get(tracking=tracking)
    affiliation = Affiliations.objects.get(resume=resume.pk)
    affiliation.delete()
    return Response(status=status.HTTP_200_OK) 




@api_view(['POST'])
def deleteHouseImage(request):
    resume = Resume.objects.get(tracking=tracking)
    affiliation = Affiliations.objects.get(resume=resume.pk)
    affiliation.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def deleteHouse(request):
    resume = Resume.objects.get(tracking=tracking)
    affiliation = Affiliations.objects.get(resume=resume.pk)
    affiliation.delete()
    return Response(status=status.HTTP_200_OK)


# @api_view(['POST'])
# def register(request):
#     resume = Resume.objects.get(tracking=tracking)
#     affiliation = Affiliations.objects.get(resume=resume.pk)
#     affiliation.delete()
#     return Response(status=status.HTTP_200_OK)

# @api_view(['POST'])
# def login(request):
#     resume = Resume.objects.get(tracking=tracking)
#     affiliation = Affiliations.objects.get(resume=resume.pk)
#     affiliation.delete()
#     return Response(status=status.HTTP_200_OK)


# @api_view(['POST'])
# def resetPassword(request):
#     resume = Resume.objects.get(tracking=tracking)
#     affiliation = Affiliations.objects.get(resume=resume.pk)
#     affiliation.delete()
#     return Response(status=status.HTTP_200_OK)


# @api_view(['POST'])
# def changePassword(request):
#     resume = Resume.objects.get(tracking=tracking)
#     affiliation = Affiliations.objects.get(resume=resume.pk)
#     affiliation.delete()
#     return Response(status=status.HTTP_200_OK)





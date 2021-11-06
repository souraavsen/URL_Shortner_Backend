from shorturl.models import *
from rest_framework import serializers
from accounts.serializers import UserSerializer

class ForAnonymousSerializer(serializers.ModelSerializer):
    class Meta:
        model= Short_URL
        fields ="__all__"
        extra_kwargs = {'short_url': {'required': False},'currentuser': {'required': False}}

class CustomUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model= Short_URL
        fields ="__all__"
        extra_kwargs = {'short_url': {'required': False}}


class ShortUrlSerializerview(serializers.ModelSerializer):
    class Meta:
        model= Short_URL
        fields = "__all__"
        
class EditUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model= Short_URL
        fields = "__all__"
        extra_kwargs = {'main_url': {'required': False},'currentuser': {'required': False}}
        

class ShortUrlSerializer(serializers.ModelSerializer):
    currentuser=UserSerializer( read_only=True)
    class Meta:
        model= Short_URL
        fields = "__all__"


from .models import (
        Fan, 
        Artist, 
        ArtistProfile, 
        Release,
        Product
    )
from rest_framework import serializers


class FanRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fan
        fields = ('password','email','name')

class FanLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fan
        fields = ('password','email')


class ArtistRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('password','email','name')

class ArtistLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('password','email')

class ArtistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile
        fields = '__all__'

class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ('id','title','urls','slug','photo','created_on','artist_name','artist')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','url','embed_code','created_on','created_on','artist_name', 'artist')
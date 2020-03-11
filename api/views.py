from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import filters
import jwt
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password, make_password
from .models import (
        Fan, 
        Artist, 
        ArtistProfile, 
        Release,
        Product
    )
from .serializers import (
        FanRegisterSerializer, 
        FanLoginSerializer,
        ArtistRegisterSerializer, 
        ArtistLoginSerializer,
        ArtistProfileSerializer, 
        ReleaseSerializer,
        ProductSerializer
    )

class FanRegisterView(viewsets.ModelViewSet):
    queryset =  Fan.objects.all()
    serializer_class = FanRegisterSerializer
    http_method_names = ['post']

    def create(self, request):
        data     = request.data
        name     = data["name"]
        password = data["password"]
        email    = data["email"]

        token = jwt.encode({'email': email}, 'secret', algorithm='HS256').decode('ascii')

        obj  = Fan.objects.create(email = email, name = name, password= make_password(password), token=token)

        if obj:
            return JsonResponse({"code":200, "msg": "sucess"})
        return JsonResponse({"code":400, "msg": "failed"})


class FanLoginView(viewsets.ModelViewSet):
    queryset =  Fan.objects.all()
    serializer_class = FanLoginSerializer
    http_method_names = ['post']

    def create(self, request):
        data     = request.data
        password = data["password"]
        email    = data["email"]

        count = Fan.objects.filter(email=email).count()
        if count > 0:
            hashed_password = list(Fan.objects.filter(email=email).values('password'))[0]["password"]
            password=check_password(password, hashed_password)
            if password:
                token = jwt.encode({'email': email}, 'secret', algorithm='HS256').decode('ascii')
                return JsonResponse({"code":200, "msg": "sucess", "token": token})
        return JsonResponse({"code":400, "msg": "failed"})     


class ArtistRegisterView(viewsets.ModelViewSet):
    queryset =  Artist.objects.all()
    serializer_class = ArtistRegisterSerializer
    http_method_names = ['post']

    def create(self, request):
        data     = request.data
        name     = data["name"]
        password = data["password"]
        email    = data["email"]

        token = jwt.encode({'email': email}, 'secret', algorithm='HS256').decode('ascii')

        obj      = Artist.objects.create(email = email, name = name, password= make_password(password), token=token)

        if obj:
            return JsonResponse({"code":200, "msg": "sucess"})
        return JsonResponse({"code":400, "msg": "failed"})


class ArtistLoginView(viewsets.ModelViewSet):
    queryset =  Artist.objects.all()
    serializer_class = ArtistLoginSerializer
    http_method_names = ['post']

    def create(self, request):
        data     = request.data
        password = data["password"]
        email    = data["email"]

        count = Artist.objects.filter(email=email).count()
        if count > 0:
            hashed_password = list(Artist.objects.filter(email=email).values('password'))[0]["password"]
            password=check_password(password, hashed_password)
            if password:
                token = jwt.encode({'email': email}, 'secret', algorithm='HS256').decode('ascii')
                return JsonResponse({"code":200, "msg": "sucess", "token": token})
        return JsonResponse({"code":400, "msg": "failed"})


class ArtistProfileView(viewsets.ModelViewSet):
    queryset =  ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer


class ReleaseView(viewsets.ModelViewSet):
    queryset =  Release.objects.all()
    serializer_class = ReleaseSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'title', 'slug','created_on']

    def get_queryset(self):
        queryset = Release.objects.all()

        title = self.request.query_params.get('title', None)
        slug = self.request.query_params.get('slug', None)
        artist_name = self.request.query_params.get('artist_name', None)
        artist_id = self.request.query_params.get('artist_id', None)
        date_range = self.request.query_params.get('date_range', None)

        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        
        if slug is not None:
            queryset = queryset.filter(slug=slug)
            
        if artist_name is not None:
            queryset = queryset.filter(artist__name=artist_name)

        if artist_id is not None:
            queryset = queryset.filter(artist=artist_id)

        if date_range is not None:
            queryset = queryset.filter(created_on__range=eval(date_range))

        return queryset


class ProductView(viewsets.ModelViewSet):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'created_on']

    def get_queryset(self):
        queryset = Product.objects.all()

        name = self.request.query_params.get('name', None)
        artist_name = self.request.query_params.get('artist_name', None)
        artist_id = self.request.query_params.get('artist_id', None)

        if artist_name is not None:
            queryset = queryset.filter(artist__name=artist_name)
        
        if artist_id is not None:
            queryset = queryset.filter(artist=artist_id)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
            
        if date_range is not None:
            queryset = queryset.filter(created_on__range=eval(date_range))
            
        return queryset
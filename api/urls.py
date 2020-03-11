from rest_framework import routers
from .views import (
      FanRegisterView, 
      FanLoginView,
      ArtistRegisterView, 
      ArtistLoginView,
      ArtistProfileView, 
      ReleaseView,
      ProductView
   )
from django.urls import path, include

router = routers.DefaultRouter()
router.register('fan-register', FanRegisterView)
router.register('fan-login', FanLoginView)
router.register('artist-register', ArtistRegisterView)
router.register('artist-login', ArtistLoginView)
router.register('profile', ArtistProfileView)
router.register('release', ReleaseView)
router.register('product', ProductView)


urlpatterns = [
   path(r'', include(router.urls)),
]
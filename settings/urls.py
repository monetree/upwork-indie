from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_swagger_view(title='Swgger root')


urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('', include("api.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

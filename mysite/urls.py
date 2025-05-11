from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movieapp.views import MovieViewSet,ActionViewSet,ComedyViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register(r'action', ActionViewSet, basename='action-movies')
router.register(r'comedy', ComedyViewSet, basename='comedy-movies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

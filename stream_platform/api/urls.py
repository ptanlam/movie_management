from django.urls import path

from .views import StreamPlatformListAV, StreamPlatformDetailAV

urlpatterns = [
    path('', StreamPlatformListAV.as_view()),
    path('<int:platform_pk>/', StreamPlatformDetailAV.as_view()),
]

from django.urls import path

from .views import StreamPlatformListAV, StreamPlatformDetailAV

urlpatterns = [
    path('stream-platforms/', StreamPlatformListAV.as_view()),
    path('stream-platforms/<int:pk>/', StreamPlatformDetailAV.as_view()),
]

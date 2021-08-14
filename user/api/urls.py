from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

from .views import registration_view

urlpatterns = [
    path('login/', obtain_auth_token),
    path('register/', registration_view),
]

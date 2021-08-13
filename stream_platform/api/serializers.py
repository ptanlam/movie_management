from rest_framework import serializers

from movie.api.serializers import MovieSerializer
from ..models import StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'

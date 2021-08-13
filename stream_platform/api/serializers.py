from rest_framework import serializers

from movie.api.serializers import MovieSerializer
from ..models import StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"

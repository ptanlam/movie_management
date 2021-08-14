from rest_framework import serializers

from ..models import Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('movie',)


class MovieSerializer(serializers.ModelSerializer):
    stream_platforms = serializers.StringRelatedField(many=True, read_only=True)
    avg_rating = serializers.ReadOnlyField()
    number_of_ratings = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = '__all__'

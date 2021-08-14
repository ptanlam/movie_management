from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import status, generics

from stream_platform.models import StreamPlatform
from stream_platform.api.serializers import StreamPlatformSerializer

from ..models import Movie, Review

from .permissions import IsAuthorOrReadOnly
from .serializers import (MovieSerializer, ReviewSerializer)


class ReviewListForMovie(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        movie_pk = self.kwargs.get('movie_pk')
        return Movie.objects.get(pk=movie_pk).reviews.all()

    def perform_create(self, serializer):
        movie_pk = self.kwargs.get('movie_pk')
        movie = Movie.objects.get(pk=movie_pk)

        author = self.request.user
        reviews = Review.objects.filter(movie=movie,
                                        author=author)

        if reviews.exists():
            raise ValidationError('You have already reviewed this movie.')

        serializer.save(movie=movie, author=author)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_object(self):
        review_pk = self.kwargs.get('review_pk')
        return Review.objects.get(pk=review_pk)


class MovieListAV(APIView):
    def get(self, request: Request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = MovieSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)


class MovieDetailAV(APIView):
    def get(self, request: Request, movie_pk: int):
        try:
            movie = Movie.objects.get(id=movie_pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, movie_pk: int):
        movie = Movie.objects.get(id=movie_pk)
        serializer = MovieSerializer(movie, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, movie_pk: int):
        movie = Movie.objects.get(id=movie_pk)
        movie.delete()
        return Response(status=status.HTTP_200_OK)


class StreamPlatformListForMovieAV(APIView):
    def get(self, request: Request,
            movie_pk: int):
        try:
            stream_platforms = Movie.objects.get(pk=movie_pk) \
                .stream_platforms
            serializer = StreamPlatformSerializer(stream_platforms,
                                                  many=True)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            print("hi")
            return Response(status=status.HTTP_404_NOT_FOUND)


class StreamPlatformDetailForMovieAV(APIView):
    def get(self, request: Request,
            movie_pk: int, platform_pk: int):
        try:
            stream_platform = StreamPlatform.objects.get(pk=platform_pk)
            serializer = StreamPlatformSerializer(stream_platform)
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

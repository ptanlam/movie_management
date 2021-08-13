from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status, generics, mixins

from ..models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer


class ReviewList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


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
        movie = Movie.objects.get(id=movie_pk)
        try:
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

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

from django.urls import path

from .views import (MovieListAV, MovieDetailAV,
                    StreamPlatformListForMovieAV,
                    StreamPlatformDetailForMovieAV,
                    ReviewListForMovie, ReviewDetail)

urlpatterns = [
    path('', MovieListAV.as_view()),
    path('<int:movie_pk>', MovieDetailAV.as_view(), name='movie-detail'),

    path('<int:movie_pk>/platforms/', StreamPlatformListForMovieAV.as_view()),
    path('<int:movie_pk>/platforms/<int:platform_pk>',
         StreamPlatformDetailForMovieAV.as_view()),

    path('<int:movie_pk>/reviews/', ReviewListForMovie.as_view()),
    path('<int:movie_pk>/reviews/<int:review_pk>', ReviewDetail.as_view()),
]

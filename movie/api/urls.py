from django.urls import path

from .views import MovieListAV, MovieDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('', MovieListAV.as_view()),
    path('<int:movie_pk>', MovieDetailAV.as_view(), name='movie-detail'),

    path('<int:movie_pk>/reviews/', ReviewList.as_view()),
    path('<int:movie_pk>/reviews/<int:review_pk>', ReviewDetail.as_view()),
]

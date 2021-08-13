from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from stream_platform.models import StreamPlatform


class Movie(models.Model):
    title = models.CharField(max_length=250)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    stream_platform = models.ManyToManyField(StreamPlatform,
                                             related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(5)])
    movie = models.ForeignKey('Movie',
                              on_delete=models.CASCADE,
                              related_name='reviews')
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.movie.title} | {self.rating}'

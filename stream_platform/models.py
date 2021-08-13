from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

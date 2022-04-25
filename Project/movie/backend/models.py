from django.db import models
from uuid import uuid4
from django_mysql.models import ListCharField

# Create your models here.
class Ratting(models.Model):
    adult = models.BooleanField(default=False)
    backdrop_path = models.ImageField(upload_to='images')
    original_language = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    overview = models.CharField(max_length=10000)
    popularity = models.DecimalField(max_digits=7, decimal_places=3)
    poster_path = models.CharField(max_length=255)
    release_date = models.DateField(auto_created=None)
    title = models.CharField(max_length=255)
    video = models.BooleanField(default=False)
    vote_average = models.DecimalField(max_digits=2, decimal_places=1)
    vote_count = models.IntegerField()

    def __str__(self):
        return self.title



class MovieRatting(models.Model):
    # uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=255)
    genre_ids = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11),  # 6 * 10 character nominals, plus commas
    )
    movie_id = models.IntegerField()
    original_language = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    overview = models.CharField(max_length=10000)
    popularity = models.DecimalField(max_digits=7, decimal_places=3)
    poster_path = models.CharField(max_length=255)
    release_date = models.DateField(auto_created=None)
    title = models.CharField(max_length=255)
    video = models.BooleanField(default=False)
    vote_average = models.DecimalField(max_digits=2, decimal_places=1)
    vote_count = models.IntegerField()


    def __str__(self):
        return self.title
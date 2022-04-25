from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, db_index=True)
    # birth_date = models.DateField(null=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile = models.ImageField(upload_to='images')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username


    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
   
        
class Ratting(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=255)
    original_language = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    overview = models.CharField(max_length=300)
    popularity = models.DecimalField(max_digits=7, decimal_places=3)
    poster_path = models.CharField(max_length=255)
    release_date = models.DateField(auto_created=None)
    title = models.CharField(max_length=255)
    video = models.BooleanField(default=False)
    vote_average = models.DecimalField(max_digits=2, decimal_places=1)
    vote_count = models.IntegerField()

    def __str__(self):
        return self.title

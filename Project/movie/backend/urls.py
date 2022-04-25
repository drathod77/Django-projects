from django.urls import path
from .views import *

urlpatterns = [
    path('data/',view),
    path('home/',home,name='home'),
    path('api/',requestapi,name='api'),
    path("home/<int:pk>/", movie_detail, name="movie_detail"),
]

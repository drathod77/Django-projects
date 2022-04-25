from django.urls import path
from .views import *

urlpatterns = [
    path('', readCsv, name='download'),
]

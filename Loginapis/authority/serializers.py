from rest_framework import serializers
from .models import Ratting


class MovieSerializer(serializers.ModelSerializer):
     class Meta:
         model = Ratting
         fields = '__all__'

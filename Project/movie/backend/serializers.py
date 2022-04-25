from rest_framework import serializers
from .models import Ratting,MovieRatting

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratting
        fields = '__all__'

class MovieSerializerAPI(serializers.ModelSerializer):
    adult=serializers.BooleanField()
    backdrop_path= serializers.CharField()
    original_language = serializers.CharField()
    overview = serializers.CharField()
    poster_path = serializers.CharField()
    release_date = serializers.DateField()
    vote_average = serializers.DecimalField(max_digits=2, decimal_places=1)
    vote_count = serializers.IntegerField()
    class Meta:
        model = Ratting
        fields = ['adult','backdrop_path','original_language']

        # def create(self, validated_data):
        #     return Ratting.objects.create(**validated_data)

class MainSerializer(serializers.Serializer):
    page=serializers.IntegerField()
    total_pages=serializers.IntegerField()
    results = MovieSerializerAPI(many=True)
    total_results=serializers.IntegerField()

    def create(self, validated_data):
        return Ratting.objects.create(
            adult=validated_data['results']['adult'],
            backdrop_path=validated_data['results']['backdrop_path']
        )


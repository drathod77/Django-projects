from rest_framework import serializers


class ProductSerializer(serializers.Serialize):
    Id = serializers.IntegerField(read_only=False)
    

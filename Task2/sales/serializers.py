from rest_framework import serializers
from .models import SalesModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesModel
        fields = '__all__'

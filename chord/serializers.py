from rest_framework import serializers
from .models import Tone

class Serializer(serializers.ModelSerializer):
    class Meta:
        model=Tone
        fields='__all__'
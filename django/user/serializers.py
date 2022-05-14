from dataclasses import field
from rest_framework import serializers
from .models import User, Pet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        field = '__all__'
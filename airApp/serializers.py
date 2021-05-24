from rest_framework import serializers

from .models import House, User, HouseType

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields=['id','name','address','price','booked','owner','roomtype']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','phone','email']


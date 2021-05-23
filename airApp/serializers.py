from rest_framework import serializers

from .models import House, User, HouseType

class HouseSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # roomtype = serializers.PrimaryKeyRelatedField(queryset=HouseType.objects.all())
    class Meta:
        model = House
        fields=['id','name','address','price','booked','owner','roomtype']

class UserSerializer(serializers.ModelSerializer):
    house = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['name','phone','email','house']


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

class BookHouseSerializer(serializers.Serializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    roomtype = serializers.PrimaryKeyRelatedField(
        queryset=HouseType.objects.all(),
        many=True
    )
    def create(self, validated_data):
        house = self.context.get("house")

        if not house.booked:
            house.booked = True
            house.owner = validated_data.get("owner")
            # house.roomtype.add(validated_data.get("roomtype").values_list("id", flat=True))
            house.roomtype.add(
                *[room.id for room in validated_data.get("roomtype",[])]
            )
            house.save()
        
        return house
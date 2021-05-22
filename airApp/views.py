from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from airApp.models import User, House
from airApp.serializers import UserSerializer, HouseSerializer

# Create your views here.

class Userviewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class Houseviewset(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = House.objects.all()

@api_view(['POST'])
def book_house(req,pk):
    print(req.data)
    try:
        house = House.objects.get(pk=pk)

    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        user = User.objects.get(name= req.data.owner)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    req.data.owner = user.id

    # print(req.data)
    # print(req.data.owner)
    
    if house.booked == False:
        # house.booked = True
        # house.owner = req.data.owner
        # house.roomtype = req.data.roomtype
        # house.save()
        serializer = HouseSerializer(house, data=req.data)
        print("checking")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"Error":"error"},status=status.HTTP_400_BAD_REQUEST)
    
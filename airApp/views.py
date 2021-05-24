from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from airApp.models import User, House, HouseType
from airApp import (
    serializers as air_app_serializers
)

# Create your views here.


class Userviewset(viewsets.ModelViewSet):
    serializer_class = air_app_serializers.UserSerializer
    queryset = User.objects.all()

class Houseviewset(viewsets.ModelViewSet):
    serializer_class = air_app_serializers.HouseSerializer
    queryset = House.objects.all()

# @api_view(['POST'])
# def book_house(req,pk):
#     import pdb 
#     pdb.set_trace()
#     try:
#         house = House.objects.filter(pk=pk).first()
#     except House.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     try:
#         user = User.objects.filter(name= req.data.get("owner")).first()
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     try:
#         housetype = HouseType.objects.get(name= req.data.get("roomtype"))
#     except HouseType.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if house.booked == False:
#         house.booked = True
#         house.owner = user
#         house.roomtype.add(housetype)
#         house.save()
#         return Response({"Udated":"updated"},status=status.HTTP_201_CREATED)
#         # serializer = HouseSerializer(house, data=req.data)
#         # print("checking")
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response({"Error":"error"},status=status.HTTP_400_BAD_REQUEST)
    
class BookViewSet(CreateAPIView):
    serializer_class = air_app_serializers.BookHouseSerializer

    def get_serializer_context(self):
        response = super().get_serializer_context()
        house_pk = self.kwargs.get("pk")
        house = House.objects.filter(pk=house_pk).first()
        if not house:
            raise Http404()

        response["house"] = house
        return response

        
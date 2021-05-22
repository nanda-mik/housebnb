from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class HouseType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class House(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    booked = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='house', null=True, blank=True)
    roomtype = models.ForeignKey(HouseType, on_delete=models.CASCADE, default="", related_name='house',null=True, blank=True)

    def __str__(self):
        return self.name 


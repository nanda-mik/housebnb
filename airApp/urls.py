from rest_framework import routers
from django.urls import path

from . import views

router = routers.SimpleRouter()
router.register(r'users', views.Userviewset)
router.register(r'house',views.Houseviewset)

urlpatterns = [
    path('book/<int:pk>', views.book_house, name="book")
]
# passing the house id as parameter which is to be booked
urlpatterns += router.urls
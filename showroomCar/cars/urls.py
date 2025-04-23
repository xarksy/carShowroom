from django.urls import path
from .views import carList, create_car, detail_car,deleteCar, updateCar

urlpatterns = [
    path('',carList,name='carList'),
    path('create/', create_car, name='create_car'),
    path('detail/<int:car_id>/', detail_car, name='detail_car'),
    path('delete/<int:car_id>/', deleteCar, name='delete_car'),
    path('update/<int:car_id>/', updateCar, name='update_car'),
]

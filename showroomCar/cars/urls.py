from django.urls import path
from .views import carList, create_car, detail_car,deleteCar, updateCar, car_service,car_service_plain

urlpatterns = [
    path('',carList,name='carList'),
    path('create/', create_car, name='create_car'),
    path('detail/<int:car_id>/', detail_car, name='detail_car'),
    path('delete/<int:car_id>/', deleteCar, name='delete_car'),
    path('update/<int:car_id>/', updateCar, name='update_car'),
    path('service/', car_service_plain, name='car_service'),
    path('service/<int:car_id>/', car_service, name='service_history'),
    path('service/<int:car_id>/delete/<int:service_id>/', car_service, name='delete_service_history'),
    path('service/<int:car_id>/update/<int:service_id>/', car_service, name='update_service_history'),
]

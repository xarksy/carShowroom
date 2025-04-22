from django.urls import path
from .views import carList

urlpatterns = [
    path('',carList,name='carList'),
]

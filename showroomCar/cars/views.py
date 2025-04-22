from django.shortcuts import render, get_object_or_404, redirect
from .models import Cars
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def carList(request):
    """
    View to display the list of cars in the showroom.
    """
    
    # Render the template with the list of cars
    return render(request, 'cars/index.html')

def carDetail(request, car_id):
    pass

def addCar(request):
    pass

def updateCar(request, car_id):
    pass

def deleteCar(request, car_id):
    pass

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cars
from .forms import CarsForm
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def carList(request):
    """
    View to display the list of cars in the showroom.
    """
    context = {
        'cars': Cars.objects.all()  # Fetch all car objects from the database
    }
    # Render the template with the list of cars
    return render(request, 'cars/index.html', context)

def create_car(request):
    """
    View to create a new car entry in the showroom.
    """
    if request.method == 'POST':
        # Handle form submission
        pass  # Implement form handling logic here
    else:
        # Render the form for creating a new car
        pass  # Implement form rendering logic here
    return render(request, 'cars/car_form.html')


def carDetail(request, car_id):
    pass

def updateCar(request, car_id):
    pass

def deleteCar(request, car_id):
    pass

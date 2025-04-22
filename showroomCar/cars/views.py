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
        form = CarsForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the new car instance to the database
            form.save()
            # Redirect to the car list page after successful creation
            return redirect('carList')
        else:
            # Log the form errors for debugging purposes
            logger.error("Form submission failed: %s", form.errors)
        # Handle form submission
        pass  # Implement form handling logic here
    else:
        form = CarsForm()

    context = {
        'form': form  # Pass the form to the template for rendering
    }
        # Render the form for creating a new car
    return render(request, 'cars/car_form.html', context=context)


def carDetail(request, car_id):
    pass

def updateCar(request, car_id):
    pass

def deleteCar(request, car_id):
    pass

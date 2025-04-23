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


def detail_car(request, car_id):
    """
    View to display the details of a specific car.
    """
    # Fetch the car object using the provided car_id
    car = get_object_or_404(Cars, id=car_id)
    context = {
        'car': car  # Pass the car object to the template for rendering
    }
    # Render the template with the car details
    return render(request, 'cars/detail.html', context)


def updateCar(request, car_id):
    """
    View to update the details of a specific car.
    """
    # Fetch the car object using the provided car_id
    car = get_object_or_404(Cars, id=car_id)
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            # Save the updated car instance to the database
            form.save()
            # Redirect to the car list page after successful update
            return redirect('carList')
        else:
            # Log the form errors for debugging purposes
            logger.error("Form submission failed: %s", form.errors)
    else:
        form = CarsForm(instance=car)

    context = {
        'form': form  # Pass the form to the template for rendering
    }
    # Render the form for updating the car details
    return render(request, 'cars/car_form.html', context=context)

def deleteCar(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    car.delete()
    return redirect('carList')

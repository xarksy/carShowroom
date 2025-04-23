from django.shortcuts import render, get_object_or_404, redirect
from .models import Cars, ServiceHistory
from .forms import CarsForm, ServiceHistoryForm
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
    service_history = car.service_histories.all()  # Fetch the service history entries for the car
    total_biaya = sum(service.biaya for service in service_history)
    context = {
        'car': car,  # Pass the car object to the template for rendering
        'service_history': service_history,  # Pass the service
        'total_biaya': total_biaya,
        'cash': total_biaya + car.harga,  # Pass the total service cost to the template for rendering
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

def car_service_plain(request):
    """
    View to manage the service history of cars in the showroom.
    """
    if request.method == 'POST':
        form = ServiceHistoryForm(request.POST)
        if form.is_valid():
            # Create a new service history entry
            form.save()
            return redirect('carList')  # Redirect to the car list page after successful creation
    else:
        form = ServiceHistoryForm()

    context = {
        'form': form  # Pass the form to the template for rendering
    }
    # Render the form for managing service history
    return render(request, 'cars/service_history_form.html', context=context)

def car_service(request, car_id):
    """
    View to manage the service history of a specific car.
    """
    # Fetch the car object using the provided car_id
    car = get_object_or_404(Cars, id=car_id)
    if request.method == 'POST':
        form = ServiceHistoryForm(request.POST, request.FILES, hide_car_field=True)
        if form.is_valid():
            # Create a new service history entry for the car
            service_history = form.save(commit=False)
            service_history.car = car  # Associate the service history with the car
            service_history.save()  # Save the service history instance to the database
            return redirect('detail_car', car_id=car.id)  # Redirect to the car detail page after successful creation
    else:
        # Pre-fill the form with the current car_id
        form = ServiceHistoryForm(initial={'mobil': car.id}, hide_car_field=True)
        # Set the initial value for the car field in the form
        # form.fields['mobil'].initial = car.id

    context = {
        'form': form,  # Pass the form to the template for rendering
        'car': car  # Pass the car object to the template for rendering
    }
    # Render the form for managing service history
    return render(request, 'cars/service_history_form.html', context=context)
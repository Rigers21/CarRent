from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from cars.forms import ReservationForm
from cars.models import Car, Reservation


@csrf_exempt
def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {
        'cars': cars
    })


def about(request):
    return HttpResponse('<h1>Welcome to About page <h1>')


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    reservations = Reservation.objects.filter(car=car)
    return render(request, 'detail.html', {
        'car': car,
        'reservations': reservations
    })


@login_required
def reserve(request, car_id):
    car = Car.objects.get(pk=car_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if Reservation.objects.filter(car=car, start_date__lte=end_date, end_date__gte=start_date).exists():
                messages.error(request, 'The selected dates are not available for reservation!')
            else:
                Reservation.objects.create(car=car, start_date=start_date, end_date=end_date, user=request.user)
                messages.success(request, 'Car reserved successfully!')
                return redirect('detail', car_id=car_id)

    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {
        'car': car,
        'form': form
    })


@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)
    reservation.delete()
    return redirect('detail', reservation.car.id)

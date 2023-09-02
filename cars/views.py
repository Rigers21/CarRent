from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage
from .forms import ContactForm
from cars.forms import ReservationForm
from cars.models import Car, Reservation


@csrf_exempt
def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {
        'cars': cars
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'The message was sent successfully!')
            return redirect('thankyou')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    reservations = Reservation.objects.filter(car=car)
    return render(request, 'detail.html', {
        'car': car,
        'reservations': reservations
    })


@login_required()
def reserve(request, car_id):
    car = Car.objects.get(pk=car_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if end_date < start_date:
                messages.error(request, 'End date must be later than the start date!')
            elif Reservation.objects.filter(car=car, start_date__lte=end_date, end_date__gte=start_date).exists():
                messages.error(request, 'The selected dates are not available for reservation!')
            else:
                Reservation.objects.create(car=car, start_date=start_date, end_date=end_date, user=request.user)
                messages.success(request, 'Car reserved successfully!')


    else:
        form = ReservationForm()

    initial_start_date = now().date()
    form.fields['start_date'].initial = initial_start_date
    return render(request, 'reservation.html', {
        'car': car,
        'form': form
    })


@login_required()
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if end_date < start_date:
                messages.error(request, 'End date must be later than the start date!')
            elif Reservation.objects.filter(car=reservation.car, start_date__lte=end_date,
                                          end_date__gte=start_date).exclude(pk=reservation_id).exists():
                messages.error(request, 'The selected dates are not available for reservation!')
            else:
                reservation.start_date = start_date
                reservation.end_date = end_date
                reservation.save()

                messages.success(request, 'Reservation updated successfully!')


    else:
        form = ReservationForm(initial={'start_date': reservation.start_date, 'end_date': reservation.end_date})
    return render(request, 'update_reservation.html', {
        'reservation': reservation,
        'form': form
    })


@login_required()
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)
    reservation.delete()
    return redirect('detail', reservation.car.id)

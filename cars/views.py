from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from cars.models import Car


@csrf_exempt
def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {
        'cars': cars
    })


def about(request):
    return HttpResponse('<h1>Welcome to About page <h1>')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {
        'email': email
    })


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'detail.html', {
        'car': car,
    })

from django.urls import path
from . import views

urlpatterns = [
    path('<int:car_id>', views.detail, name='detail'),
    path('<int:car_id>/reserve', views.reserve, name='reserve'),
    path('reservation/<int:reservation_id>', views.update_reservation, name='updatereservation'),
    path('reservation/<int:reservation_id>/delete', views.delete_reservation, name='deletereservation'),

]

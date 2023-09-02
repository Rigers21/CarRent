from django.contrib import admin
from .models import Car, Reservation, ContactMessage


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields['user'].initial = request.user
            form.base_fields['user'].widget.attrs['readonly'] = True
        return form


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'name',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields['email'].initial = request.email
            form.base_fields['email'].widget.attrs['readonly'] = True
        return form


class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:  # Creating a new reservation
            form.base_fields['model'].initial = request.model
            form.base_fields['model'].widget.attrs['readonly'] = True
        return form


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)

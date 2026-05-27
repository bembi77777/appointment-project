from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import AppointmentForm
from .models import Appointment


def home(request):

    if request.method == 'POST':

        form = AppointmentForm(request.POST)

        if form.is_valid():

            appointment = form.cleaned_data

            existing = Appointment.objects.filter(
                appointment_date=appointment['appointment_date'],
                appointment_time=appointment['appointment_time']
            ).exists()

            if existing:
                messages.error(
                    request,
                    "This appointment slot is already booked."
                )
            else:
                form.save()
                messages.success(
                    request,
                    "Appointment booked successfully!"
                )
                return redirect('/')

    else:
        form = AppointmentForm()

    return render(
        request,
        'home.html',
        {'form': form}
    )
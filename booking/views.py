from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm

def home(request):

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
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
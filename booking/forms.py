from django import forms
from datetime import date
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            'customer_name',
            'phone_number',
            'appointment_date',
            'appointment_time'
        ]

    def clean_appointment_date(self):

        appointment_date = self.cleaned_data['appointment_date']

        if appointment_date < date.today():
            raise forms.ValidationError(
                "You cannot book an appointment in the past."
            )

        return appointment_date
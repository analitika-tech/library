from django import forms

from datetime import datetime
from datetime import date

from backend.models import Book, Class, Student, Issue, Reservation

class DateInput(forms.DateInput):
    input_type = 'date'


def date_convert(date):
    return datetime.strptime(date, "%Y-%m-%d")

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        
        labels = {
            'name': 'Naziv djela',
            'author': 'Autor djela',
            'year': 'Godina izdanja',
            'quantity': 'Količina'
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
    
        labels = {
            'first_name': 'Ime',
            'last_name': 'Prezime',
            'classes': 'Razred',
        }

class IssueForm(forms.ModelForm):
    leaseDate = forms.DateField(widget = DateInput, label = "Datum iznajmljivanja")

    class Meta:
        model = Issue
        fields = ["reservation", "student", "leaseDate",]
        
        labels = {
            'reservation': 'Rezervacija',
            'student': 'Učenik',
        }
    # Lease date
    def clean_leaseDate(self, *args, **kwargs):
        date = self.cleaned_data["leaseDate"]
        if date >= datetime.today().date():
            return date
        raise forms.ValidationError("Datum koji ste unijeli nije validan!")

    def clean(self, *args, **kwargs):
        reservation = Reservation.objects.get(id = self.cleaned_data["reservation"].id)

        # Checking to not exceed quantity
        if reservation.issued >= reservation.quantity:
            raise forms.ValidationError(f"Ne možete izdati više knjiga jer su rezervisane samo { reservation.quantity } knjige!")

        # Checking if the lease date is in range of the reservation dates
        if self.cleaned_data["leaseDate"] < reservation.startDate or self.cleaned_data["leaseDate"] > reservation.endDate:
            raise forms.ValidationError(f"Ne možete rezervisati knjigu, jer period za koji je knjiga rezervisana je { reservation.startDate } - { reservation.endDate }")

        return self.cleaned_data

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["startDate", "endDate", "book", "quantity",]

        labels = {
            'book': 'Knjiga',
            'quantity': 'Količina',
        }

    startDate = forms.DateField(widget = DateInput, label = "Početak rezervacije")
    endDate = forms.DateField(widget = DateInput, label = "Kraj rezervacije")

    # Checking if the start date is valid 
    def clean_startDate(self, *args, **kwargs):
        date = self.cleaned_data["startDate"]
        if date >= datetime.today().date():
            return date
        raise forms.ValidationError("Datum koji ste unijeli nije validan!")

    # Checking if the end date is valid 
    def clean_endDate(self, *args, **kwargs):
        date = self.cleaned_data["endDate"]
        if date >= datetime.today().date():
            return date
        raise forms.ValidationError("Datum koji ste unijeli nije validan!")
    
    # Checking the reservaed quantity to the total quantity
    def clean_quantity(self, *args, **kwargs):
        book, quantity = self.cleaned_data["book"], self.cleaned_data["quantity"]
        if quantity <= book.quantity:
            return quantity
        raise forms.ValidationError(f'Trenutno stanje knjige "{ book }" je { self.cleaned_data["book"].quantity }')
    
    # Checking the date range
    def clean(self, *args, **kwargs):
        startDate, endDate = self.clean_startDate(), self.clean_endDate()
        
        if endDate > startDate:
            return self.cleaned_data
        raise forms.ValidationError("Opseg datuma nije validan!")
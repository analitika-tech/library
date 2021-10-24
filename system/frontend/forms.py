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

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class IssueForm(forms.ModelForm):
    startDate = forms.DateField(widget = DateInput)
    endDate = forms.DateField(widget = DateInput)

    class Meta:
        model = Issue
        fields = ["reservation", "student", "startDate", "endDate",]

    def clean_startDate(self, *args, **kwargs):
        date = self.cleaned_data["startDate"]
        if date >= datetime.today().date():
            return date
        raise forms.ValidationError("Datum koji ste unijeli nije validan!")

    # def clean_endDate(self, *args, **kwargs):
    #     date = self.cleaned_data["endDate"]
    #     if date >= datetime.today().date():
    #         return date
    #     raise forms.ValidationError("Datum koji ste unijeli nije validan!")

    def clean(self, *args, **kwargs):
        reservation = Reservation.objects.get(id = self.cleaned_data["reservation"].id)
        if reservation.issued >= reservation.quantity:
            raise forms.ValidationError(f"Ne možete izdati više knjiga jer su rezervisane samo { reservation.quantity } knjige!")
        return self.cleaned_data

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["startDate", "endDate", "book", "quantity",]

    startDate = forms.DateField(widget = DateInput)
    endDate = forms.DateField(widget = DateInput)

    def clean_startDate(self, *args, **kwargs):
        date = self.cleaned_data["startDate"]
        if date >= datetime.today().date():
            return date
        raise forms.ValidationError("Datum koji ste unijeli nije validan!")

    def clean_endDate(self, *args, **kwargs):
        date = self.cleaned_data["endDate"]
        if date >= datetime.today().date():
            return date
        raise forms.ValidationError("Datum koji ste unijeli nije validan!")
    
    def clean_quantity(self, *args, **kwargs):
        book, quantity = self.cleaned_data["book"], self.cleaned_data["quantity"]
        if quantity <= book.quantity:
            return quantity
        raise forms.ValidationError(f'Trenutno stanje knjige "{ book }" je { self.cleaned_data["book"].quantity }')
    
    def clean(self, *args, **kwargs):
        startDate, endDate = self.clean_startDate(), self.clean_endDate()

        if endDate > startDate:
            return self.cleaned_data
        raise forms.ValidationError("Opseg datuma nije validan!")
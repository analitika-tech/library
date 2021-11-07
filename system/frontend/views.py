from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.views import View

# Decorators
from django.utils.decorators import method_decorator
from .decorators import allowerd_users

from datetime import date

# Models and Forms
from backend.models import Book, Class, Student, Issue, Reservation
from .forms import BookForm, ClassForm, StudentForm, IssueForm, ReservationForm
from .custom import get_fields


def home_view(request):
    books = Book.objects.all()
    fields = []
    # Model field list
    for field in Book._meta.get_fields():
        if field.name != "reservation":
            fields.append(field.name) 

    context = {
        "querySet": books,
        "fields": fields,
    }

    return render(request, "home.html", context)

def error_view(request):
    return render(request, "components/error.html")

class BookGPView(View):
    @method_decorator(allowerd_users(["book-editing"]))
    def get(self, request):
        books = Book.objects.all()
        form = BookForm()
        fields = []

        # Model field list
        for field in Book._meta.get_fields():
            if field.name != "reservation":
                fields.append(field.name) 

        context = {
            "fields": fields,
            "querySet": books,
            "form": form,
        }

        return render(request, "book/index.html", context)

    @method_decorator(allowerd_users(["book-editing"]))
    def post(self, request):
        form = BookForm()

        if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("book-view")
            else:
                return form.errors

class BookPDView(View):
    def get_object(self, pk):
        try:
            return Book.objects.get(id = pk)
        except Book.DoesNotExist:
            raise Http404
    
    @method_decorator(allowerd_users(["book-editing"]))
    def get(self, request, pk):
        return self.get_object(pk)
    
    @method_decorator(allowerd_users(["book-editing"]))
    def put(self, request, pk):
        book = self.get_object(pk)
        data = {}

        if request.is_ajax():
            form = BookForm(instance = book, data = request.POST)
            if form.is_valid():
                form.save()
                data['code'] = 200
                data['content'] = "Uspješno ste izmjenili podatke o njizi!"
                return JsonResponse(data)
            
            data["content"] = form.errors
            return JsonResponse(data)

    @method_decorator(allowerd_users(["book-editing"]))
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return JsonResponse(dict(code = 204, content = "Knjiga je izbrisana"))


class StudentGPView(View):
    @method_decorator(allowerd_users(["student-editing"]))
    def get(self, request):
        students = Student.objects.all()
        form = StudentForm()
        fields = []

        # Model fields
        for field in Student._meta.get_fields():
            if field.name != "issue":
                fields.append(field.name)


        context = {
            "fields": fields,
            "querySet": students,
            "form": form,
        }

        return render(request, "student/index.html", context)

    @method_decorator(allowerd_users(["student-editing"]))
    def post(self, request):
        form = StudentForm()

        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("student-view")
            else:
                return form.errors

class StudentPDView(View):
    def get_object(self, pk):
        try:
            return Student.objects.get(id = pk)
        except Student.DoesNotExist:
            raise Http404

    @method_decorator(allowerd_users(["student-editing"]))
    def get(self, request, pk):
        return self.get_object(pk)
    
    @method_decorator(allowerd_users(["student-editing"]))
    def put(self, request, pk):
        book = self.get_object(pk)
        data = {}

        if request.is_ajax():
            form = BookForm(instance = book, data = request.POST)
            if form.is_valid():
                form.save()
                data['code'] = 200
                data['content'] = "Uspješno ste izmjenili podatke o njizi!"
                return JsonResponse(data)
            
            data["content"] = form.errors
            return JsonResponse(data)
    
    @method_decorator(allowerd_users(["student-editing"]))
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return JsonResponse(dict(code = 204, content = "Učenik je izbrisan!"))


class ReservationGPView(View):
    @method_decorator(allowerd_users(["reservation-editing"]))
    def get(self, request):
        reservation = Reservation.objects.all()
        form = ReservationForm()
        fields = get_fields(Reservation, "issue")

        context = {
            "fields": fields,
            "querySet": reservation,
            "form": form,
        }

        return render(request, "reservation/index.html", context)
    
    @method_decorator(allowerd_users(["reservation-editing"]))
    def post(self, request):
        reservation = Reservation.objects.all()
        form = ReservationForm()
        fields = get_fields(Reservation, "issue")

        if request.method == "POST":
            form = ReservationForm(request.POST)
            if form.is_valid():
                form.cleaned_data["professor"] = request.user
                form.save()
                return redirect("reservation-view")
        
        context = {
            "fields": fields,
            "querySet": reservation,
            "form": form,
        }

        return render(request, "reservation/index.html", context)

class ReservationPDView(View):
    def get_object(self, pk):
        try:
            return Reservation.objects.get(id = pk)
        except Reservation.DoesNotExist:
            raise Http404
    
    @method_decorator(allowerd_users(["reservation-editing"]))
    def get(self, request, pk):
        return self.get_object(pk)
    
    # def put(self, request, pk):
    #     book = self.get_object(pk)
    #     data = {}

    #     if request.is_ajax():
    #         form = BookForm(instance = book, data = request.POST)
    #         if form.is_valid():
    #             form.save()
    #             data['code'] = 200
    #             data['content'] = "Uspješno ste izmjenili podatke o njizi!"
    #             return JsonResponse(data)
            
    #         data["content"] = form.errors
    #         return JsonResponse(data)
    
    @method_decorator(allowerd_users(["reservation-editing"]))
    def delete(self, request, pk):
        reservation = self.get_object(pk)
        
        book = Book.objects.get(id = reservation.book.id)
        book.quantity += reservation.quantity
        book.save()

        reservation.delete()
        return JsonResponse(dict(code = 204, content = "Rezervacija je izbrisana!"))


class IssueGPView(View):
    @method_decorator(allowerd_users(["issue-editing"]))
    def get(self, request):
        issues = Issue.objects.all()
        form = IssueForm()
        fields = [field.name for field in Issue._meta.get_fields()]

        context = {
            "fields": fields,
            "querySet": issues,
            "form": form,
        }

        return render(request, "issue/index.html", context)

    @method_decorator(allowerd_users(["issue-editing"]))
    def post(self, request):
        issues = Issue.objects.all()
        form = IssueForm()
        fields = [field.name for field in Issue._meta.get_fields()]

        if request.method == "POST":
            form = IssueForm(request.POST)
            if form.is_valid():
                issue = Reservation.objects.get(id = form.cleaned_data["reservation"].id)
                issue.issued += 1
                issue.save()

                form.save()
                return redirect("issue-view")

        context = {
            "fields": fields,
            "querySet": issues,
            "form": form,
        }

        return render(request, "issue/index.html", context)

class IssuePDView(View):
    # Getting the Issue object
    def get_object(self, pk):
        try:
            return Issue.objects.get(id = pk)
        except Issue.DoesNotExist:
            raise Http404

    @method_decorator(allowerd_users(["issue-editing"]))
    def get(self, request, pk):
        return self.get_object(pk)
    
    @method_decorator(allowerd_users(["issue-editing"]))
    def put(self, request, pk):
        issue = self.get_object(pk)
        data = {}

        if request.is_ajax():
            reservation = issue.reservation
            
            if issue.returnStatus:
                # Updating the issues DB to the latest info
                issue.returnStatus = False
                issue.returnDate = None
                issue.debt = 0
                reservation.returned -= 1
            else:
                issue.returnStatus = True
                issue.returnDate = date.today()
                if date.today() > reservation.endDate:
                    delta = date.today() - reservation.endDate
                    issue.debt = delta.days * .5
                reservation.returned += 1
            
            # Saving the changes
            issue.save()
            reservation.save()

            # Preparing the data for returning into template
            data['returnStatus'] = issue.returnStatus
            data['returnDate'] = issue.returnDate
            data['debt'] = issue.debt
            data['content'] = "Uspješno ste izmjenili podatke o knjizi!"

            return JsonResponse(data)
    
    @method_decorator(allowerd_users(["issue-editing"]))
    def delete(self, request, pk):
        issue = self.get_object(pk)
        issue.delete()

        return JsonResponse(dict(code = 204, content = "Učenik je izbrisan!"))


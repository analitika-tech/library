from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.views import View

from datetime import date

from backend.models import Book, Class, Student, Issue, Reservation
from .forms import BookForm, ClassForm, StudentForm, IssueForm, ReservationForm
from .custom import get_fields

def home_view(request):

    context = {}

    return render(request, "home.html", context)


class BookGPView(View):
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
    
    def get(self, request, pk):
        return self.get_object(pk)
    
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
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return JsonResponse(dict(code = 204, content = "Knjiga je izbrisana"))


class StudentGPView(View):
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
    
    def get(self, request, pk):
        return self.get_object(pk)
    
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
    
    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return JsonResponse(dict(code = 204, content = "Učenik je izbrisan!"))


class ReservationGPView(View):
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
    
    def delete(self, request, pk):
        reservation = self.get_object(pk)
        
        book = Book.objects.get(id = reservation.book.id)
        book.quantity += reservation.quantity
        book.save()

        reservation.delete()
        return JsonResponse(dict(code = 204, content = "Rezervacija je izbrisana!"))


class IssueGPView(View):
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
    def get_object(self, pk):
        try:
            return Issue.objects.get(id = pk)
        except Issue.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        return self.get_object(pk)
    
    def put(self, request, pk):
        issue = self.get_object(pk)
        data = {}

        if request.is_ajax():
            reservation = issue.reservation
            
            if issue.returnStatus:
                # Updating the issues DB to the latest info
                issue.returnStatus = False
                issue.returnDate = None
                reservation.returned -= 1
            else:
                issue.returnStatus = True
                issue.returnDate = date.today()
                if date.today() > reservation.endDate:
                    print(date.today() - reservation.endDate)
                reservation.returned += 1
            
            # Saving the changes
            issue.save()
            reservation.save()

            data['returnStatus'] = issue.returnStatus
            data['returnDate'] = issue.returnDate

            # data['returnDate'] = issue.returnDate

            data['content'] = "Uspješno ste izmjenili podatke o knjizi!"
            return JsonResponse(data)
            
            # data["content"] = form.errors
            # return JsonResponse(data)
    
    def delete(self, request, pk):
        issue = self.get_object(pk)
        issue.delete()
        return JsonResponse(dict(code = 204, content = "Učenik je izbrisan!"))

from django.shortcuts import render, redirect

from django.http import Http404, JsonResponse
from django.views import View

from backend.models import Book, Class, Student, Issue, Reservation
from .forms import BookForm, ClassForm, StudentForm, IssueForm, ReservationForm

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
            if field.name != "issues":
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
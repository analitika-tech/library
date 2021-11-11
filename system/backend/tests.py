from django.test import TestCase, Client
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory

from prettytable import PrettyTable
from secrets import token_hex
import json

# Models
from .models import Book, Class, Student, Reservation, Issue
from .serializers import BookSerializer, ClassSerializer, StudentSerializer
# Views
from .views import BookAPIView, ClassAPIView, StudentAPIView

# Data
from .data import books, classes, students, reservations, issues, paths

# Testing the basic model functionality

# Book model testing
class BackendTest(TestCase):
    def __init__(self, *args, **kwargs):
        # Global params
        self.password = token_hex(15)
        self.username = "backend.testing"
        self.factory = APIRequestFactory()
    
        # Creating the superuser
        # self.user = User.objects.create_superuser(username = self.username, password = self.password)
        
        # Global lists
        self.views = [BookAPIView.as_view(), ClassAPIView.as_view(), StudentAPIView.as_view()]
        self.bookData, self.classData, self.studentData = [], [], []

        super(BackendTest, self).__init__(*args, **kwargs)

    def setUp(self):
        """Inserting data into the models"""
        
        # Book model
        for book in books:
            Book.objects.create(name = book[0], author = book[1], year = book[2], quantity = book[3])
        self.bookData.append(Book.objects.all())
        
        # Class model
        for clss in classes:
            Class.objects.create(name = clss[0], professor = clss[1])
        self.classData.append(Class.objects.all())

        # Student model
        for student in students:
            Student.objects.create(first_name = student[0], last_name = student[1], classes = Class.objects.get(name = student[2]))
        self.studentData.append(Student.objects.all())
            
        # Reservation model
        for reservation in reservations:
            Reservation.objects.create(
                startDate = reservation[0], 
                endDate = reservation[1], 
                professor = reservation[2], 
                book = Book.objects.get(name = reservation[3]), 
                quantity = reservation[4])

        # Issues model
        for issue in issues:
            Issue.objects.create(
                reservation = Reservation.objects.get(id = issue[0]),
                student = Student.objects.get(id = issue[1]),
                leaseDate = issue[2])
            
    def test_querySet_all(self):
        test1 = Book.objects.all()
        test2 = Class.objects.all()
        test3 = Student.objects.all()
        test4 = Reservation.objects.all()
        test5 = Issue.objects.all()
    

        table = PrettyTable(["Book", "Class", "Student", "Reservation", "Issue"])
        for (book, clss, student, reservation, issue) in zip(test1, test2, test3, test4, test5):
            table.add_row([book, clss, student, reservation, issue])
        print(table)
        
                
    def test_api_get(self):
        """Testing the get method on the apis"""
        login = self.client.login(username = self.username, password = self.password)      
        
        for (path, view) in zip(paths, self.views):
            request = self.factory.get(path)
            response = view(request)
            print(response)

    def test_api_delte(self):
        """Testing the delete method on the apis"""
        login = self.client.login(username = self.username, password = self.password)      
               
        for (path, view) in zip(paths, self.views):
            request = self.factory.delete(path)
            response = view(request)
            print(response)


        

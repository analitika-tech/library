from django.test import TestCase, Client
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory

from prettytable import PrettyTable
from secrets import token_hex
import json

from .models import Book, Class, Student, Reservation, Issue # Models
from .views import BookAPIView, ClassAPIView, StudentAPIView # Views
from .data import books, classes, students, reservations, issues, paths # Data for testing ./data.py

class BackendTest(TestCase):
    def __init__(self, *args, **kwargs):
        # Global params
        self.password = token_hex(15)
        self.username = "backend.testing"
        self.factory = APIRequestFactory()
        self.views = [BookAPIView.as_view(), ClassAPIView.as_view(), StudentAPIView.as_view()] # API Views
        
        # Creating super user if it not exists
        if not User.objects.filter(username = self.username).exists():
            self.user = User.objects.create_superuser(username = self.username, password = self.password)            

        super(BackendTest, self).__init__(*args, **kwargs)

    def setUp(self):
        """Inserting data into the models"""
        
        # Book model
        for book in books:
            Book.objects.create(name = book[0], author = book[1], year = book[2], quantity = book[3])
        
        # Class model
        for clss in classes:
            Class.objects.create(name = clss[0], professor = clss[1])

        # Student model
        for student in students:
            Student.objects.create(first_name = student[0], last_name = student[1], classes = Class.objects.get(name = student[2]))
            
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
            self.assertTrue(response.status_code, 200)
        self.client.get("logout/")

    def test_api_delte(self):
        """Testing the delete method on the apis"""
        login = self.client.login(username = self.username, password = self.password)      
               
        for (path, view) in zip(paths, self.views):
            request = self.factory.delete(path)
            response = view(request)
            self.assertTrue(response.status_code, 204)
        self.client.get("logout/")

    def test_api_post(self):
        """Testing the post method on the apis"""
        login = self.client.login(username = self.username, password = self.password)      
        
        # Formating the data
        dataSet = [
             [{"name": book[0], "author": book[1], "year": book[2], "quantity": book[3]} for book in books],
             [{"name": clss[0], "professor": clss[0]} for clss in classes],
             [{"first_name": student[0], "last_name": student[1], "classes": Class.objects.get(name = student[2]).id} for student in students]
        ]

        for (path, data, view) in zip(paths, dataSet, self.views):
            request = self.factory.post(path, json.dumps(data, indent = 4), content_type = "application/json")
            response = view(request)
            self.assertTrue(response.status_code, 201)
        self.client.get("logout/")

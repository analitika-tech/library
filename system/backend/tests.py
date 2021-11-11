from django.test import TestCase, Client
from datetime import date, timedelta
from prettytable import PrettyTable

# Models
from .models import Book, Class, Student, Reservation, Issue

# Book Model Fields = name:str, author:str, year:int, quantity:int
books = [
    ["Oliver Twist", "Charles Dickens", 1838, 50],
    ["The Little Prince", "Antoine de Saint-Exupéry", 1943, 150],
    ["The Old Man and the Sea", "Ernest Hemingway", 1952, 30],
    ["Romeo and Juliet", "William Shakespeare", 1597, 10],
    ["Hamlet", "William Shakespeare", 1603, 50]]


# Class Model Fields = name:str, professor:str
classes = [
    ["Class 1", "Prof 1"],
    ["Class 2", "Prof 2"],
    ["Class 3", "Prof 3"]]


# Student Model Fields = first_name:str, last_name:str, classes:Foreign Key
students = [
    ["Rajon", "Rondo", classes[0][0]],
    ["Leborn", "James", classes[1][0]],
    ["Russell", "Westbrook", classes[2][0]]]


# Reservation Model Fields = startDate:date, endData:date, professor:str, book:Foreign Key, quantity:int, returned:int, issued:int, returnStatus:bool
reservations = [
    [date.today(), date.today() + timedelta(20), "Prof 1", "Oliver Twist", 15],
    [date.today(), date.today() + timedelta(10), "Prof 2", "Romeo and Juliet", 10],
    [date.today(), date.today() + timedelta(15), "Prof 3", "The Old Man and the Sea", 20]]

# Issue Model Fields = reservation:Foreign Key, student: Foreign Key, leaseDate: date, returnDate: date, returnStatus: bool, deb:int
issues = [
    [1, 1, date.today() + timedelta(1)],
    [2, 2, date.today() + timedelta(3)],    
    [3, 3, date.today() + timedelta(5)]]

# Testing the basic model functionality

# Book model testing
class BackendTest(TestCase):
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
        
            
    

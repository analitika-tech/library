from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length = 500)
    author = models.CharField(max_length = 300)
    year = models.IntegerField(default = 2000)
    quantity = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return str(self.name)

class Class(models.Model):
    name = models.CharField(max_length = 50)
    professor = models.CharField(max_length = 1000)

    def __str__(self) -> str:
        return str(self.name)

class Student(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{ self.first_name } { self.last_name }"    

class Reservation(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    professor = models.CharField(max_length = 3000, blank = True, null = True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    returned = models.IntegerField(default = 0) # Nuber of returned book's
    issued = models.IntegerField(default = 0) # Number of issued book's
    returnStatus = models.BooleanField(default = False) # Return status changes to true when all book's are returned

    # Checking if all of the issued book's are returned and upatding the status of the reservation 
    def save(self, *args, **kwargs):
        if self.issued == self.returned:
            self.returnStatus = True
        else: 
            self.returnStatus = False
            
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{ self.id } - { self.book } - { self.professor }"


class Issue(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete = models.CASCADE, null = True, blank = True)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    leaseDate = models.DateField()
    returnDate = models.DateField(blank = True, null = True)
    returnStatus = models.BooleanField(default = False)
    debt = models.DecimalField(max_digits = 30, decimal_places = 2, default = '0')

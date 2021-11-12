from datetime import date, timedelta
# Book Model Fields = name:str, author:str, year:int, quantity:int
books = [
    ["Oliver Twist", "Charles Dickens", 1838, 50],
    ["The Old Man and the Sea", "Ernest Hemingway", 1952, 30],
    ["Romeo and Juliet", "William Shakespeare", 1597, 10]]

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

# API paths
paths = ["bookapi/", "classapi/", "studentapi/"]

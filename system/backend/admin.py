from django.contrib import admin
from .models import Book, Class, Student

admin.site.register(Book)
admin.site.register(Class)
admin.site.register(Student)
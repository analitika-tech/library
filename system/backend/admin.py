from django.contrib import admin
from .models import Info, Book, Student, Issue, Reservation, Class

# Register your models here.

admin.site.register(Info)
admin.site.register(Book)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Issue)
admin.site.register(Reservation)
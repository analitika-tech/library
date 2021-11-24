from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book, Class, Student
from .serializers import BookSerializer, ClassSerializer, StudentSerializer


class BookAPIView(APIView):
    def get(self, request, format = None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = BookSerializer(data = request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format = None):
        Book.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ClassAPIView(APIView):
    def get(self, request, format = None):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ClassSerializer(data = request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format = None):
        Class.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class StudentAPIView(APIView):
    def get(self, request, format = None):
        person = Student.objects.all()
        serializer = StudentSerializer(person, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = StudentSerializer(data = request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format = None):
        Student.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

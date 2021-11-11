from django.test import TestCase
from backend.models import Book

class FrontendTest(TestCase):
    def test_get_data(self):
        print(Book.objects.all())


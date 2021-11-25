from django.test import TestCase
from django.contrib.auth.models import User, Group
import os, json

class FrontendTest(TestCase):

    def setUp(self, *args, **kwargs):
        # Global params
        self.groups = [group.name for group in Group.objects.all()]
        self.pages = ["/", "/tutorial/", "/book/", "/student/", "/reservation/", "/issue/", "/login/", "/logout/"]

        self.credentials = { "username": "frontend.testing", "password": "testing1" }

        # Checking if the user exists
        if not User.objects.filter(username = self.credentials["username"]).exists():
            user = User.objects.create_user(**self.credentials)
            user.save()
        
        # Checking if the user has the required groups
        user = User.objects.get(username = self.credentials["username"])
        for name in self.groups:
            if not user.groups.filter(name = name).exists():
                Group.objects.get(name = name).user_set.add(user)

        # Logging in
        self.user = self.client.login(**self.credentials)

    def test_main_sites(self):
        """The main sites include the home page and the help page"""        

        for page in self.pages[:2]:
            self.assertEqual(self.client.get(page).status_code, 200)
    
    def test_pages_is_authenticated(self):
        """Testing available pages when the user is authenticated"""

        for page in self.pages[2:6]:
            self.assertEqual(self.client.get(page, follow = True).status_code, 200)

    def test_book_post_request(self):
        """Testing the POST request for book page"""

        books = [
            { "name": "Oliver Twist", "author": "Charles Dickens", "year": 1838, "quantity": 100 },
            { "name": "Madame Bovary", "author": "Gustave Flaubert", "year": 1856, "quantity": 100 },
            { "name": "Ana Karenjina", "author": "Lav Nikolajevič Tolstoj", "year": 1877, "quantity": 100 }
        ]
        
        for book in books:
            self.assertEqual(self.client.post("/book/", book, content_type = "application/json", follow = True).status_code, 200)
    
    
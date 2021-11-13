from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from secrets import token_hex

class FrontendTest(StaticLiveServerTestCase):
    def __init__(self, *args, **kwargs):
        # Global params
        self.username = "frontend.testing"
        self.password = token_hex(15)
        
        if not User.objects.filter(username = self.username).exists():
            User.objects.create(username = self.username, password = self.password)

        super(FrontendTest, self).__init__(*args, **kwargs)

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/login')

        username = driver.find_element_by_id("id_username")
        password = driver.find_element_by_id("id_password")
        submit = driver.find_element_by_id("register_button")

        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.send_keys(Keys.RETURN)

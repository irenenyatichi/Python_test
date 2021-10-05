from django.forms.widgets import EmailInput
from django.test import TestCase
from .models import User

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User(
            email = "irenenyatichik@gmail.com",
            password = "dghkj100",
            project_name = "Irene Nyatichi",
            simulation_name = "default simulation"
        )

    def test_email(self):
        self.assertIn(self.user.email,"irenenyatichik@gmail.com")

    def test_password(self):
        self.assertEqual(self.user.password,'dghkj100')

    def test_project_name(self):
        self.assertEqual(self.user.project_name , "Irene Nyatichi")

    def test_simulation_name(self):
        self.assertEqual(self.user.simulation_name , "default simulation")
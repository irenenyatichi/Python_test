from django.db import models
from django.forms.widgets import EmailInput
from django.test import TestCase
from .models import User,  Project,  Simulation

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email = "irenenyatichik@gmail.com",
            password = "dghkj100",
        )
        self.project = Project.objects.create(
            # user=User(email = "irenenyatichik@gmail.com",password = "dghkj100"),
            project_name = "Irene Nyatichi",
            project_description = "This project is based on the assessment given.",
        )
        self.simulation = Simulation.objects.create(
            # project=Project(project_name = "Irene Nyatichi",project_description = "This project is based on the assessment given."),
            simulation_name = "First Simulation",
            date = "2021-10-05",
        )


    def test_login_credentials(self):
        self.assertEqual(self.user.email,"irenenyatichik@gmail.com" )
        self.assertEqual(self.user.password, "dghkj100")


    def test_create_project(self):
        user = self.user
        self.assertTrue(isinstance(self.user , User))
        self.assertEqual(self.project.project_name,"Irene Nyatichi")
        self.assertEqual(self.project.project_description,"This project is based on the assessment given.")


    def test_simulation(self):
        project = self.project
        self.assertTrue(isinstance(self.project and self.user , User))
        self.assertEqual(self.simulation.simulation_name, "First Simulation")
        self.assertEqual(self.simulation.date, "2021-10-05")

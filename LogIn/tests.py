from django.db import models
from django.forms.widgets import EmailInput
from django.test import TestCase
from .models import User,  Project,  Simulation

# The Tests

class UserTestCase(TestCase):
# Details based on an account created.
    def setUp(self):
        self.user = User.objects.create(
            email = "irenenyatichik@gmail.com",
            password = "dghkj100",
        )
        self.project = Project.objects.create(
            project_name = "Irene Nyatichi",
            project_description = "This project is based on the assessment given.",
        )
        self.simulation = Simulation.objects.create(
            simulation_name = "First Simulation",
            date = "2021-10-05",
        )


    def test_login_credentials(self):
    #To ensure that the user is logged in.
        self.assertEqual(self.user.email,"irenenyatichik@gmail.com" )
        self.assertEqual(self.user.password, "dghkj100")


    def test_create_project(self):
    #To ensure that the user is logged in before creating a project.
        user = self.user     
        self.assertTrue(isinstance(self.user , User))   
    #This is the code for testing the creation of the project
        self.assertEqual(self.project.project_name,"Irene Nyatichi")
        self.assertEqual(self.project.project_description,"This project is based on the assessment given.")


    def test_simulation(self):
    #To ensure that the logged in user has a project before simulating it.
        project = self.project  
        self.assertTrue(isinstance(self.project and self.user , User))
    #This is the code for testing the simulation of the project
        self.assertEqual(self.simulation.simulation_name, "First Simulation")
        self.assertEqual(self.simulation.date, "2021-10-05")
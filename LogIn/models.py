from django.db import models
from django.db.models.expressions import Value
from django.conf import settings
from django.db import models


class User(models.Model):
    email=models.EmailField(max_length=30, default='irene@gmail.com')
    password = models.CharField(max_length=15, default='irene1234')

class Project(models.Model):
    project_name = models.TextField(max_length=50 , default= "project_name")
    project_description = models.CharField(max_length=500 , default="project description")

class Simulation(models.Model):
    simulation_name = models.CharField(max_length=30, default="default simulation")
    date = models.DateField()

class Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)

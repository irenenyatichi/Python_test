from django.db import models
from django.db.models.expressions import Value
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class User(models.Model):
    email=models.EmailField(max_length=30, default='Email')
    password = models.CharField(max_length=15, default='Password')

class Project(models.Model):
    project_name = models.TextField(max_length=50 , default= "Project Name")
    project_description = models.CharField(max_length=500 , default="Project Description")

class Simulation(models.Model):
    simulation_name = models.CharField(max_length=30, default="Simulation Name")
    date = models.DateField()

class Details(models.Model):
    user = models.ManyToOneRel(User,to=Project and Simulation, on_delete=models.CASCADE, field_name = None)
    project = models.OneToOneRel(Project, to=Simulation, on_delete=models.CASCADE, field_name = None)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)

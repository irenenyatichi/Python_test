from django.db import models
from django.db.models.expressions import Value
from django.db.models.fields import CharField
# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=30)
    password = models.CharField(max_length=15)
    project_name = models.TextField(max_length=50 , default= "project_name")
    project_description = models.CharField(max_length=500 , default="project description")
    simulation_name = models.CharField(max_length=30, default="default simulation")

def __str__(self):
    return self.email

def create_project(self):
    return f"{self.project_name} {self.project_decription}"

def simulate(self):
    return f"{self.simulation_name} {self.project_name} {self.project_decription}" 
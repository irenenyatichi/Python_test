from django.urls import path

from .views import  register_user, start_simulation, create_project
urlpatterns=[
    path("register/",register_user,name="register_user"),
    path("project/",create_project, name="create_project"),
    path("simulation/",start_simulation, name="start_simulation")
]
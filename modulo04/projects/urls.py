from django.urls import path
from .import views

urlpatterns = [
    path("adicionar-projeto/", views.adicionar_projeto, name= "adicionar_projeto"),
]
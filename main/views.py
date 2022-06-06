from django.shortcuts import render
from django.views import generic

class Home(generic.ListView):
    template_name = "base.html"
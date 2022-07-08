from django.shortcuts import render
from django.views import generic

class Home(generic.View):
    template_name = "base.html"
    
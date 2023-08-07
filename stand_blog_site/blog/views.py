from django.views.generic import ListView, DetailView
from django.shortcuts import render

# class Home(ListView):
#   template_name = 'blog/index.html'


def index(request):
    return render(request, template_name="blog/index.html")

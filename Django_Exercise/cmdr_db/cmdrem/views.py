from django.shortcuts import render
from django.views.generic import ListView
from .models import CmdRemember
# Create your views here.

class HomePageView(ListView):
    model=CmdRemember
    template_name='index.html'
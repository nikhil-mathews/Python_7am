from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Article
from django.views.generic import ListView,DeleteView
# Create your views here.

class HomePageView(ListView):
    model=Article
    template_name='home.html'

class DetailPageView(DetailView):
    model=Article
    template_name='detail.html'
    context_object_name='superman'
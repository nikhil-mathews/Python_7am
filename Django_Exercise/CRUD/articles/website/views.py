from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Article
from django.views.generic import ListView,DeleteView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
    model=Article
    template_name='home.html'

class DetailPageView(DetailView):
    model=Article
    template_name='detail.html'
    context_object_name='superman'

class CreatePageView(CreateView):
    model=Article
    template_name='create.html'
    fields='__all__'

class EditPageView(UpdateView):
    model=Article
    template_name='update.html'
    fields=['title','desc']

class DeletePageView(DeleteView):
    model=Article
    template_name='delete.html'
    context_object_name='superman'
    success_url=reverse_lazy('home')
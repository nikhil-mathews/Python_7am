from django.urls import path
from . import views
# https://127.0.0.1:8000

urlpatterns = [
    path('',views.homePage,name='home'),
    
]

from django.urls import path
from .import views
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('article/<int:pk>',views.DetailPageView.as_view(),name='article-detail')
]

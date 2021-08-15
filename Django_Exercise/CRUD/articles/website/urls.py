from django.urls import path
from .import views
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('article/<int:pk>',views.DetailPageView.as_view(),name='article-detail'),
    path('article/new',views.CreatePageView.as_view(),name='article-new'),
    path('article/edit/<int:pk>',views.EditPageView.as_view(),name='article-edit'),
    path('article/delete/<int:pk>',views.DeletePageView.as_view(),name='article-delete'),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    # path('about/', views.article_list),
]

# Create the routes

from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from .views import about_nj_view
  
urlpatterns = [
    path('', about_nj_view , name="about_nj_view"),
]
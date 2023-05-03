from django.urls import path
from demo1 import views
urlpatterns = [
    path('contact/', views.stud),
    path('', views.home),
    path('signin/',views.sign),
    
]

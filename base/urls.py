from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="home"),
    path('about/', views.AboutPage, name="about"),
    path('service2/', views.Service2Page, name="service2"),
    path('service3/', views.Service3Page, name="service3"),
    path('single-service/', views.SingleService, name="single-service"),
    path('book/', views.BookingPage, name="book"),
    path('contact/', views.contactPage, name="contact"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contactUs, name='contact_us'),
]

from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('',views.index),
    path('about/',views.about, name='about'),
    path('contact/',views.contact),
    path('profile/',views.profile),
    path('note/',views.note , name='note'),
    path('userlogout/',views.userlogout),
    path('conform/',views.conform, name='conform'),
]
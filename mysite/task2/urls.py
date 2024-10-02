from django.urls import path
from . import views
from .views import *

#python mysite/manage.py runserver

urlpatterns = [
    path("", index),
    path('function/', views.function_view, name='function_view'),
    path('class/', views.ClassView.as_view(), name='class_view'),
]

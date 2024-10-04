from django.urls import path
from . import views
from .views import *

#python mysite/manage.py runserver

urlpatterns = [
    path("", index),
    path('other/', views.other_view, name='other_view'),
    path('shop/', views.shop_view, name='shop_view'),
]

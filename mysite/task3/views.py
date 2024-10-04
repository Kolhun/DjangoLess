from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("<h2>Мой сайт task3</h2>")


# Create your views here.
def shop_view(request):
    return render(request, 'third_task/shop_view.html')


def other_view(request):
    return render(request, 'third_task/other_view.html')

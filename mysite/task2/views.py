from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("<h2>Мой первый сайт</h2>")


# Create your views here.
def function_view(request):
    return render(request, 'second_task/function_view.html')


class ClassView(TemplateView):
    template_name = 'second_task/class_view.html'

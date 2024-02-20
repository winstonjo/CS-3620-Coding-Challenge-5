from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
from .models import Portfolio
from django.template import loader


# Create your views here.


def index(request):
    context = {}
    return render(request, 'Home/index.html', context)


def hobbies(request):
    hobbies_list = Hobby.objects.all()
    context = {
        'hobbies_list': hobbies_list,
    }
    return render(request, 'Home/index.html', context)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)


def contact(request):
    return HttpResponse('email: winstonjo@mail.weber.edu')


def detail(request, id):
    hobby = Hobby.objects.get(pk=id)
    context = {
        'hobby': hobby
    }
    return render(request, 'Home/detail.html', context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hobby, Portfolio

# Create your views here.


def index(request):
    context = {}
    return render(request, 'Home/index.html', context)


def hobbies(request):
    hobbies_list = Hobby.objects.all()
    context = {
        'hobbies_list': hobbies_list,
    }
    return render(request, 'Home/hobbies.html', context)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list': portfolio_list,
    }
    return render(request, 'Home/portfolio.html', context)


def contact(request):
    return render(request, 'Home/contact.html')


def hobby_detail(request, hobby_id):
    hobby = get_object_or_404(Hobby, pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'Home/hobby_detail.html', context)


def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'Home/portfolio_detail.html', context)



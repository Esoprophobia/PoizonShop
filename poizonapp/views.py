from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

menu = [{'title': 'Каталог', 'url_name': 'catalog'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Корзина', 'url_name': 'cart'},
        {'title': 'Войти', 'url_name': 'login'}
]

def index(request):
    return render(request, 'poizonapp/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'poizonapp/about.html', {'menu': menu, 'title': 'О сайте'})


def catalog(request):
    return render(request, 'poizonapp/catalog.html', {'menu': menu, 'title': 'Каталог'})


def cart(request):
    return render(request, 'poizonapp/cart.html', {'menu': menu, 'title': 'Корзина'})


def login(request):
    return render(request, 'poizonapp/login.html', {'menu': menu, 'title': 'Авторизация'})

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

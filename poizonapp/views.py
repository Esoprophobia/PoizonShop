from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'poizonapp/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'poizonapp/about.html', {'title': 'О сайте'})


def catalog(request):
    return render(request, 'poizonapp/catalog.html', {'title': 'Каталог'})


def cart(request):
    return render(request, 'poizonapp/cart.html', {'title': 'Корзина'})


def login(request):
    return render(request, 'poizonapp/login.html', {'title': 'Авторизация'})


def logout(request):
    return render(request, 'poizonapp/logout.html', {'title': 'Выход'})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def search(request):
    return render(request, 'poizonapp/search.html', {'title': 'Поиск'})


def profile(request):
    return render(request, 'poizonapp/profile.html', {'title': 'Профиль'})

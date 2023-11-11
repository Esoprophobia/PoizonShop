from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='user_profile'),
]

from django.contrib import admin
from django.urls import path, include
from poizonapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('poizonapp.urls'))
]

handler404 = views.page_not_found

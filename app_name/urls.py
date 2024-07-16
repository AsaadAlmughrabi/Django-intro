from django.contrib import admin
from django.urls import path
from .views import HomePageVeiw,AboutPageVeiw,ContactPageVeiw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageVeiw.as_view(),name='Home'),
    path('about',AboutPageVeiw.as_view(),name='about'),
    path('contactUs',ContactPageVeiw.as_view() , name='contactUs'),
]

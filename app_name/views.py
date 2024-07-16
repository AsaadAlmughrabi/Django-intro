from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageVeiw(TemplateView):
    template_name = 'home.html'

class AboutPageVeiw(TemplateView):
    template_name = 'About.html'

class ContactPageVeiw(TemplateView):
    template_name = 'contactUs.html'
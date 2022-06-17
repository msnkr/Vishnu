from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Products

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'vish_app/home-page.html'


class ProductListView(ListView):
    model = Products


class ProductDetailView(DetailView):
    pass


class ContactView(TemplateView):
    template_name = 'vish_app/contact-us.html'
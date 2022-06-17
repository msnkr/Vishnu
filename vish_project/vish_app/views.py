from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .models import Products
from .forms import ContactPageForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'vish_app/home-page.html'


class ProductListView(ListView):
    model = Products


class ProductDetailView(DetailView):
    model = Products


class ContactView(FormView):
    template_name = 'vish_app/contact-us.html'
    form_class = ContactPageForm
    success_url = '/thanks/'

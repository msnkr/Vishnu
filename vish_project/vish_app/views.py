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


def ContactPageView(request):
    form = ContactPageForm()
    if request.method == 'POST':
        form = ContactPageForm(request.POST)
        if form.is_valid():
            form.save()
            return thank_you(request)
        else:
            return ValidationError('Error')
    else:
        return render(request, 'vish_app/contact-us.html', {'form':form})


def thank_you(request):
    return render(request, 'vish_app/thank-you.html')
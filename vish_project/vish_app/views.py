from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .models import Products
from .forms import ContactPageForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'vish_app/home-page.html'
    model = Products
    ordering = ['-date']
    
    

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        return context


class ProductListView(ListView):
    model = Products
    ordering = ['-date']


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
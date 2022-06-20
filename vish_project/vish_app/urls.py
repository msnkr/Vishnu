from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, ProductListView, ProductDetailView, ContactPageView, thank_you

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('products/', ProductListView.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail-view'),
    path('contact-us/', ContactPageView, name='contact-us'),
    path('contact-us/thank-you', thank_you, name='thank-you'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
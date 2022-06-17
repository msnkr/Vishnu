from django.urls import path
from .views import HomePageView, ProductListView, ProductDetailView, ContactView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='detail-view'),
    path('contact-us/', ContactView.as_view(), name='contact-us'),
]
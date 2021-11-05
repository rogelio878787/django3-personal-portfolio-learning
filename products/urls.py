from django.urls import path
from .views import ProductListView, checkout, ProductDetailView, add_to_cart, login_view

urlpatterns = [
    path('',ProductListView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('products/<slug>/', ProductDetailView.as_view(), name='product'),
    path('add_to_car/<slug>/', add_to_cart, name='add-to-car'),
    path('login/', login_view, name='login')

]
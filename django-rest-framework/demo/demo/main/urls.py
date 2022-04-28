from django.urls import path

from demo.main.views import ProductsListView, SingleProductView, CategoryListView

urlpatterns = [
    path('products/',ProductsListView.as_view(),name='products list'),
    path('products/<int:pk>/',SingleProductView.as_view(),name='single product'),
    path('categories/',CategoryListView.as_view(),name='categories list'),
]
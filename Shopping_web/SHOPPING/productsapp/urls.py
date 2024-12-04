from django.urls import path
from productsapp import views

urlpatterns = [
    path("", views.index),
    path("detail/<int:id>", views.productDetail, name="productDetail"),
    path("products", views.products, name="products"),
]
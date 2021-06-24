from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/list/create/', views.ProductList.as_view(), name='product_list'),
    path('api/v1/detail/<int:pk>/', views.ProductDetail.as_view(), name='product_detail')
]
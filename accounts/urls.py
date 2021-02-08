from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('update_customer/<int:pk>/',
         views.update_customer, name='update_customer'),
    path('delete_customer/<int:pk>/',
         views.delete_customer, name='delete_customer'),
    path('create_product/', views.create_product, name='create_product'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
]

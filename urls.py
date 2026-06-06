from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('products/', views.product_list, name='product_list'),

    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('add-favourite/<int:id>/', views.add_favourite, name='add_favourite'),

    path('favourites/', views.favourite_list, name='favourites'),

    path('contact/', views.contact, name='contact'),

    path('message-sent/', views.message_sent, name='message_sent'),

    path('login/', views.login_view, name='login'),
   
    path('register/', views.register_view, name='register'),
]
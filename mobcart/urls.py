from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.home, name='home'),
    path('product_list', views.product_list, name='product_list'),
    path('product_page/<int:id>/', views.product_page, name='product_page'),
    path('product_cart', views.product_cart, name='product_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_history', views.order_history, name='order_history'),
    path('thanks', views.thanks, name='thanks'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout')
]


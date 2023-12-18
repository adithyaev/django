from django.urls import path
# from customer import views (or)
from . import views

app_name = 'customer'

urlpatterns = [
    path('home',views.c_home,name ='c-home'),
    path('cart',views.c_cart,name='c-cart'),
    path('order',views.c_order,name='c-order'),
    path('wishlist',views.c_wishlist,name='c-wishlist'),
    path('profile',views.c_profile,name='c-profile'),
    
    
]
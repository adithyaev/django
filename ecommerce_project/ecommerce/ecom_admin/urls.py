from django.urls import path
from . import views

app_name = 'ecom_admin'

urlpatterns = [
    path('home',views.a_home,name='a-home'),
    path('login',views.a_login,name='a-login'),
    path('view',views.a_view_seller,name='a-view'),
]


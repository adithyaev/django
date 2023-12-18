from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('home',views.home, name='home'), 
    path('login',views.login,name='login'),  
    path('register',views.register,name='register'),
    path('masterpage',views.masterpage,name='masterpage'),
    path('extended',views.extended,name='extended'),
]
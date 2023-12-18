from django.urls import path
# from customer import views (or)
from . import views

app_name = 'seller'

urlpatterns = [
    path('home',views.s_home,name='s-home'),
    path('addproduct',views.s_add_product,name='s-addproduct'),
    path('viewproduct',views.s_view_product,name='s-viewproduct'),
    path('myprofile',views.s_my_profile,name='s-myprofile'),
]
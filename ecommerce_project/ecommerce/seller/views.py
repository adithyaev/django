from django.shortcuts import render

# Create your views here.
def s_home(request):
    return render(request, 'seller/seller_home.html')

def s_add_product(request):
    return render(request, 'seller/seller_addproduct.html')

def s_view_product(request):
    return render(request, 'seller/seller_view_product.html')

def s_my_profile(request):
    return render(request, 'seller/seller_my_profile.html')
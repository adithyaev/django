from django.shortcuts import render

# Create your views here.
def c_home(request):
    return render(request, 'customer/customer_home.html')

def c_cart(request):
    return render(request, 'customer/customer_cart.html')

def c_order(request):
    return render(request, 'customer/customer_order.html')

def c_wishlist(request):
    return render(request, 'customer/customer_wishlist.html')

def c_profile(request):
    return render(request, 'customer/customer_my_profile.html')
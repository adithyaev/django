from django.shortcuts import render

# Create your views here.
def a_home(request):
    return render(request, 'ecom_admin/admin_home.html')

def a_login(request):
    return render(request, 'ecom_admin/admin_login.html')

def a_approve_seller(request):
    return render(request, 'ecom_admin/admin_approve_seller.html')

def a_view_seller(request):
    return render(request, 'ecom_admin/admin_view_seller.html')
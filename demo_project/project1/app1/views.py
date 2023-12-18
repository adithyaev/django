from django.shortcuts import render

# Create your views here.
def home(request):
    username = 'adithya'
    items = ['python','flutter','angular','java']
    return render(request, 'app1/home.html',{'courses': items,'name':username})

def login(request):
    return render(request, 'app1/login.html')

def register(request):
    return render(request, 'app1/register.html')

def masterpage(request):
    return render(request, 'app1/masterpage.html')

def extended(request):
    return render(request, 'app1/extended.html')

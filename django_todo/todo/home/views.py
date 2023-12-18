from asyncio import Task
from sre_constants import SUCCESS
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'success': False}
    if request.method == "POST":
        # SUCCESS is {{success}}
        title = request.POST["title"]
        desc = request.POST["desc"]
        print(title,desc)
        newInstance = Task(taskTitle = title, taskDesk = desc)
        newInstance.save()
        context = { 'success':True}
    return render(request,'index.html',context)
def tasks(request):
    allTasks = Task.objects.all()
    print(allTasks)
    
    return render(request,'tasks.html')
from django.shortcuts import render
from django.shortcuts import render , redirect , get_object_or_404
from .models import Task
# Create your views here.

# list 
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'task/task_list.html',{'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('home')
    return render(request,'task_list.html')

def update_task(request,pk):
    task = get_object_or_404(Task,id=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.complete = request.POST.get('complete',False)
        task.save()
        return redirect('home')
    return render(request,'task/update_task.html',{'task':task})

def delete_task(request,pk):
    task = get_object_or_404(Task,id=pk)
    task.delete()
    return redirect('home')
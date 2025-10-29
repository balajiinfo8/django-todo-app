from django.shortcuts import render , redirect , get_list_or_404
from .models import Task
# Create your views here.

def list(request):
    task = Task.objects.all()
    return render(request,'index.html',{'task':task})
    
def add(request):
    # check the request if it was POST
    if request.method == 'POST':
        title = request.method.POST['title']
        complete = request.method.POST['complete']
        Task.objects.create(title=title,complete=complete)
        return redirect('home')
    
def update(request,pk):
    task = get_list_or_404(Task,id=pk)
    if request.method == 'POST':
        task.title =  request.POST['title']
        task.complete = 'complete' in request.POST 
        task.save()
        return redirect('home')
    return render(request,'update.html',{'task':task})

def delete(request,pk):
    task = get_list_or_404(Task,id=pk)
    task.delete()
    return redirect('home')

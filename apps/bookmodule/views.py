from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
# Create your views here.
def index(request):
# render the appropriate template for this request

    return render(request, 'bookmodule/index.html')

def tasks(request):
# render the appropriate template for this request
    Tasks = Task.objects.all()
    return render(request, 'bookmodule/tasks.html',{'Tasks': Tasks})

def task(request,tId):
# render the appropriate template for this request

    task = Task.objects.get(id = tId)
    return render(request, 'bookmodule/task.html', {'task':task})

def login(request):
# render the appropriate template for this request

    return render(request, 'bookmodule/login.html')

def logout(request):
# render the appropriate template for this request

    return render(request, 'bookmodule/logout.html')

def register(request):
# render the appropriate template for this request

    return render(request, 'bookmodule/register.html')

def create(request):
# render the appropriate template for this request
    if request.method == 'POST':
        taskobj = Task(title = request.POST.get('title'),
                                      deadline = request.POST.get('deadline'),
                                      Priority = request.POST.get('priority'),
                                      State = request.POST.get('state'),
                                      description = request.POST.get('description'))
        taskobj.save()

        return redirect('tasks')
    return render(request, 'bookmodule/create.html',{})

def edit(request,tId):
# render the appropriate template for this request
    task = Task.objects.get(id = tId)
    
    if request.method == 'POST':
        task.deadline = request.POST.get('title')
        task.deadline = request.POST.get('deadline')
        task.Priority = request.POST.get('priority')
        task.State = request.POST.get('state')
        task.description = request.POST.get('description')
        task.save()
        return redirect('task', tId = task.id )
    
    return render(request, 'bookmodule/edit.html', {'task':task})

def delete(request,bId):
# render the appropriate template for this request

    
    return render(request, 'bookmodule/delete.html', {'task_id': bId})

    
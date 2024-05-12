from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm
from .models import CheckList
from .forms import CheckListForm

# Create your views here.
def index(request):
# render the appropriate template for this request

    return render(request, 'bookmodule/index.html')

def tasks(request):
# render the appropriate template for this request
    Tasks = Task.objects.all()
    return render(request, 'bookmodule/tasks.html',{'Tasks': Tasks})


def task(request, tId):
    task = Task.objects.get(id=tId)
    checklist = CheckList.objects.filter(task = task)

    return render(request, 'bookmodule/task.html', {'task': task, 'checklist': checklist})

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
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('tasks')
    form = TaskForm(None)
    return render(request, 'bookmodule/create.html',{'form':form})

def edit(request,tId):
# render the appropriate template for this request
    task = Task.objects.get(id = tId)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('task', tId = task.id )
    form = TaskForm(instance=task)
    return render(request, 'bookmodule/edit.html', {'form':form})

def delete(request,bId):
# render the appropriate template for this request

    
    return render(request, 'bookmodule/delete.html', {'task_id': bId})

    
def createchecklist(request,tId):
# render the appropriate template for this request
    if request.method == 'POST':
        form = CheckListForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.task = Task.objects.get(id=tId)  
            obj.save()
            return redirect('task', tId = tId)
    form = CheckListForm(None)
    return render(request, 'bookmodule/createchecklist.html',{'form':form})


def editchecklist(request,tId,cId):
    checklist = CheckList.objects.get(id = cId)
    if request.method == 'POST':
        form = CheckListForm(request.POST, instance=checklist)
        if form.is_valid():
            checklist.save()
            return redirect('task', tId = tId)
    form = CheckListForm(instance=checklist)
    return render(request, 'bookmodule/editchecklist.html', {'form':form})


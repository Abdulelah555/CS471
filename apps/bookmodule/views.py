from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, CheckList
from .forms import TaskForm, CheckListForm

# Create your views here.
def index(request):
# render the appropriate template for this request

    return render(request, 'bookmodule/index.html')

def myprofile(request):
# render the appropriate template for this request

    return render(request, 'registration/myprofile.html')
def tasks(request):
# render the appropriate template for this request
    Tasks = Task.objects.all()
    
    return render(request, 'bookmodule/tasks.html',{'Tasks': Tasks})


def task(request, tId):
    task = Task.objects.get(id=tId)
    checklist_count = CheckList.objects.filter(task=task).count()
    checklist_done_count = CheckList.objects.filter(task=task,done="1").count()
    checklist = CheckList.objects.filter(task = task)

    return render(request, 'bookmodule/task.html', {'task': task, 'checklist': checklist,'checklist_count':checklist_count,'checklist_done_count':checklist_done_count})


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

def delete(request, tId):
    task = get_object_or_404(Task, id=tId)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'bookmodule/delete.html', {'task': task})

    
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


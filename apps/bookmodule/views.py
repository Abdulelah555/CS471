from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, CheckList
from .forms import TaskForm, CheckListForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'bookmodule/index.html')

@login_required
def myprofile(request):
    return render(request, 'registration/myprofile.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'bookmodule/tasks.html', {'Tasks': tasks})

@login_required
def task(request, tId):
    task = Task.objects.get(id=tId, user=request.user)
    checklist_count = CheckList.objects.filter(task=task).count()
    checklist_done_count = CheckList.objects.filter(task=task, done="1").count()
    checklist = CheckList.objects.filter(task=task)
    return render(request, 'bookmodule/task.html', {'task': task, 'checklist': checklist, 'checklist_count': checklist_count, 'checklist_done_count': checklist_done_count})

@login_required
def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
    form = TaskForm()
    return render(request, 'bookmodule/create.html', {'form': form})

@login_required
def edit(request, tId):
    task = Task.objects.get(id=tId, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task', tId=task.id)
    form = TaskForm(instance=task)
    return render(request, 'bookmodule/edit.html', {'form': form})

@login_required
def delete(request, tId):
    task = get_object_or_404(Task, id=tId, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'bookmodule/delete.html', {'task': task})

    
@login_required
def createchecklist(request, tId):
    task = Task.objects.get(id=tId, user=request.user)
    if request.method == 'POST':
        form = CheckListForm(request.POST)
        if form.is_valid():
            checklist = form.save(commit=False)
            checklist.task = task
            checklist.save()
            return redirect('task', tId=tId)
    form = CheckListForm()
    return render(request, 'bookmodule/createchecklist.html', {'form': form})


@login_required
def editchecklist(request, tId, cId):
    task = Task.objects.get(id=tId, user=request.user)
    checklist = CheckList.objects.get(id=cId, task=task)
    if request.method == 'POST':
        form = CheckListForm(request.POST, instance=checklist)
        if form.is_valid():
            form.save()
            return redirect('task', tId=tId)
    form = CheckListForm(instance=checklist)
    return render(request, 'bookmodule/editchecklist.html', {'form': form})

@login_required
def delete_checklist(request, tId, cId):
    checklist_item = get_object_or_404(CheckList, id=cId)
    if request.method == 'POST':
        checklist_item.delete()
        return redirect('task', tId=tId)
    return render(request, 'bookmodule/delete_checklist.html', {'checklist_item': checklist_item, 'task_id': tId})


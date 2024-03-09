from django.shortcuts import render

# Create your views here.
def index(request):
# render the appropriate template for this request

    return render(request, 'bookmodule/index.html')

def tasks(request):
# render the appropriate template for this request

    return render(request, 'bookmodule/tasks.html')

def task(request,bId):
# render the appropriate template for this request

    
    return render(request, 'bookmodule/task.html', {'task_id': bId})

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

    return render(request, 'bookmodule/create.html')

def edit(request,bId):
# render the appropriate template for this request

    
    return render(request, 'bookmodule/edit.html', {'task_id': bId})

def delete(request,bId):
# render the appropriate template for this request

    
    return render(request, 'bookmodule/delete.html', {'task_id': bId})

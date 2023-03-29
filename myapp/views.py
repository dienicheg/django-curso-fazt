from django.http import HttpResponse
from .models import Project, Task 
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.

def index(request):
    title = 'Bienvenido a la aplicacion de Django'
    return render(request, "index.html", {
        'title': title
    })

def about(request):
    username = 'Nicolas'
    return render(request, "about.html", {
        'username': username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        'tasks': tasks
    })
    
def create_task(request):
    if request.method == 'GET':
        #mostrar inferfaz
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
        
    else: 
        #Guardar datos
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=3)
        return redirect('tareas')
    
def create_project(request):
    if(request.method == 'GET'):
        return render(request, 'projects/create_project.html', {
                'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('proyectos')
    
def project(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/project.html', {
        'project': project,
        'tasks': tasks
    })
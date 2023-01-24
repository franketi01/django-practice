from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def index(request):
    title = "Django Course"
    return render(request , "index.html", {"title" : title})


def hello(request,username):
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    username = 'fran'
    return render(request,"about.html", {"username":username})

def projects(request):
    projects = list(Project.objects.values())
    return render(request,"projects/projects.html",{"projects":projects})

def tasks(request):
    task = Task.objects.all()
    #get_object_or_404(Task, id=id)
    return render(request,"tasks/tasks.html",{"tasks":task})

def create_task(request):  # con get se imprime las consultas como querydict
    if request.method == "GET":
        return render(request, "tasks/create_task.html", 
        {
        "form": CreateNewTask()
        }) 
    else:
        Task.objects.create(title=request.POST["title"],
        description=request.POST["description"], project_id=2)   # se crea el objeto task y se guarda
        return redirect("/tasks/")

def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {
            "form" : CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST["name"])
        return redirect("projects")

def project_detail(request,id):
    project = get_object_or_404(Project,id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "projects/details.html", {
        "project" : project,
        "tasks" : tasks
    })

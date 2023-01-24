from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"), # '' para que sea lo primero que ejecute
    path('about/',views.about, name="about"), # generamos una ventana web para el view about
    path('hello/<str:username>',views.hello, name="hello"), 
    path('projects/',views.projects, name="projects"),
    path('projects/<int:id>',views.project_detail, name="project_detail"),
    path('tasks/',views.tasks, name="tasks"),  # path('tasks/<str:title>',views.tasks),
    path('create_task/',views.create_task, name="create_task"), 
    path('create_project/',views.create_project, name="create_project"), 
]
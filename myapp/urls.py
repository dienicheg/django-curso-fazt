from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    
    # URLs proyectos
    path('projects/', views.projects, name='proyectos'),
    path('project/<int:id>', views.project, name='ver_proyecto'),
    path('create_project/', views.create_project, name='crear_proyecto'),
    
    # URLs tareas
    path('tasks/', views.tasks, name='tareas'),
    path('create_task/', views.create_task, name='crear_tarea'),
]

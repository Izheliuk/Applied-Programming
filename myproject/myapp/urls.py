from django.urls import path
from myapp import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('repair-projects/', views.repair_project_list, name='repair_project_list'),
    path('repair-projects/add/', views.add_repair_project, name='add_repair_project'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('workers/', views.worker_list, name='worker_list'),
    path('workers/add/', views.add_worker, name='add_worker'),
]

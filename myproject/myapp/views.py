from django.shortcuts import render, redirect
from myapp.repositories.client_repo import ClientRepository
from myapp.repositories.repair_project_repo import RepairProjectRepository
from myapp.repositories.task_repo import TaskRepository
from myapp.repositories.worker_repo import WorkerRepository
from myapp.forms import ClientForm, RepairProjectForm, TaskForm, WorkerForm

client_repo = ClientRepository()
repair_project_repo = RepairProjectRepository()
task_repo = TaskRepository()
worker_repo = WorkerRepository()

def client_list(request):
    clients = client_repo.get_all_clients()
    return render(request, 'client_list.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client_repo.add_client(form.cleaned_data)
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def repair_project_list(request):
    projects = repair_project_repo.get_all_projects()
    return render(request, 'repair_project_list.html', {'projects': projects})

def add_repair_project(request):
    if request.method == 'POST':
        form = RepairProjectForm(request.POST)
        if form.is_valid():
            repair_project_repo.add_project(form.cleaned_data)
            return redirect('repair_project_list')
    else:
        form = RepairProjectForm()
    return render(request, 'repair_project_form.html', {'form': form})

def task_list(request):
    tasks = task_repo.get_all_tasks()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_repo.add_task(form.cleaned_data)
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def worker_list(request):
    workers = worker_repo.get_all_workers()
    return render(request, 'worker_list.html', {'workers': workers})

def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker_repo.add_worker(form.cleaned_data)
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'worker_form.html', {'form': form})


from rest_framework import viewsets
from .models import Client, RepairProject, Task, Worker
from .serializers import ClientSerializer, RepairProjectSerializer, TaskSerializer, WorkerSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class RepairProjectViewSet(viewsets.ModelViewSet):
    queryset = RepairProject.objects.all()
    serializer_class = RepairProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import RepairProject, Task
from .serializers import RepairProjectSerializer

class ProjectReportView(APIView):
    def get(self, request):
        projects = RepairProject.objects.annotate(task_count=Count('task')).all()
        project_data = RepairProjectSerializer(projects, many=True).data
        return Response(project_data)
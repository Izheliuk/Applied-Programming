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

from django.shortcuts import render, redirect, get_object_or_404
from myapp.repositories.client_repo import ClientRepository

client_repo = ClientRepository()

def delete_client(request, client_id):
    client = get_object_or_404(Client, client_id=client_id)
    
    if request.method == 'POST':
        client_repo.delete_client(client_id)
        return redirect('client_list') 
    
    return render(request, 'confirm_delete.html', {'client': client})

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



import pandas as pd
import plotly.graph_objects as go
from django.shortcuts import render
from .models import RepairProject, Task, Worker

def generate_report(request):
    tasks = Task.objects.values('status', 'completion_date', 'worker_id')
    workers = Worker.objects.values('worker_id', 'first_name', 'last_name', 'position')

    tasks_df = pd.DataFrame(tasks)
    workers_df = pd.DataFrame(workers)

    task_counts = tasks_df['status'].value_counts()
    worker_task_counts = tasks_df['worker_id'].value_counts()
    

    bar_chart = go.Figure([go.Bar(x=task_counts.index, y=task_counts.values)])
    bar_chart.update_layout(title="Кількість задач за статусом", xaxis_title="Статус", yaxis_title="Кількість")

    scatter_chart = go.Figure([go.Scatter(
        x=tasks_df['completion_date'], 
        y=tasks_df['worker_id'],
        mode='markers',
        marker=dict(size=10)
    )])
    scatter_chart.update_layout(title="Задачі за датами завершення", xaxis_title="Дата", yaxis_title="ID працівника")

    task_timeline = tasks_df.groupby('completion_date').size()
    line_chart = go.Figure([go.Scatter(x=task_timeline.index, y=task_timeline.values, mode='lines+markers')])
    line_chart.update_layout(title="Динаміка задач", xaxis_title="Дата завершення", yaxis_title="Кількість задач")

    pie_chart = go.Figure([go.Pie(labels=worker_task_counts.index, values=worker_task_counts.values)])
    pie_chart.update_layout(title="Розподіл задач за працівниками")

    charts = {
        'bar_chart': bar_chart.to_html(full_html=False),
        'scatter_chart': scatter_chart.to_html(full_html=False),
        'line_chart': line_chart.to_html(full_html=False),
        'pie_chart': pie_chart.to_html(full_html=False),
    }

    return render(request, 'report.html', {'charts': charts})


from bokeh.resources import INLINE
from bokeh.plotting import figure
from bokeh.io import output_file, save
from bokeh.embed import components
from bokeh.palettes import Spectral11
from bokeh.models import ColumnDataSource
from bokeh.transform import cumsum
from bokeh.models import DatetimeTickFormatter
import pandas as pd
import numpy as np
from django.shortcuts import render
from .models import Task, Worker

def generate_bokeh_report(request):
    tasks = Task.objects.values('status', 'completion_date', 'worker_id')
    workers = Worker.objects.values('worker_id', 'first_name', 'last_name', 'position')

    tasks_df = pd.DataFrame(tasks)
    workers_df = pd.DataFrame(workers)

    tasks_df['completion_date'] = pd.to_datetime(tasks_df['completion_date'])

    task_counts = tasks_df['status'].value_counts()

    bar_chart = figure(title="Кількість задач за статусом", x_axis_label='Статус', y_axis_label='Кількість')
    bar_chart.vbar(x=list(task_counts.index), top=task_counts.values, width=0.9, color=Spectral11[:len(task_counts)])

    scatter_chart = figure(title="Задачі за датами завершення", x_axis_label='Дата', y_axis_label='ID працівника', tools="pan,box_zoom,reset")
    scatter_chart.scatter(x=tasks_df['completion_date'], y=tasks_df['worker_id'], size=10, color=Spectral11[0])

    task_timeline = tasks_df.groupby('completion_date').size()

    line_chart = figure(title="Динаміка задач", x_axis_label='Дата завершення', y_axis_label='Кількість задач', x_axis_type='datetime')
    line_chart.line(task_timeline.index, task_timeline.values, line_width=2)

    line_chart.xaxis.formatter = DatetimeTickFormatter(
        days="%d %b %Y",  
        months="%d %b %Y",  
        years="%Y"  
    )

    worker_data = tasks_df['worker_id'].value_counts().reset_index(name='task_count')
    worker_data['angle'] = worker_data['task_count'] / worker_data['task_count'].sum() * 2 * np.pi
    worker_data['color'] = Spectral11[:len(worker_data)] 

    source = ColumnDataSource(worker_data)

    pie_chart = figure(title="Розподіл задач за працівниками", toolbar_location=None, tools="hover", tooltips="@worker_id: @task_count")
    pie_chart.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),line_color="white", fill_color='color', legend_field='worker_id', source=source)

    bar_chart_script, bar_chart_div = components(bar_chart)
    scatter_chart_script, scatter_chart_div = components(scatter_chart)
    line_chart_script, line_chart_div = components(line_chart)
    pie_chart_script, pie_chart_div = components(pie_chart)

    bokeh_js = INLINE.render_js()
    bokeh_css = INLINE.render_css()

    return render(request, 'report_bokeh.html', {
        'bar_chart_script': bar_chart_script,
        'bar_chart_div': bar_chart_div,
        'scatter_chart_script': scatter_chart_script,
        'scatter_chart_div': scatter_chart_div,
        'line_chart_script': line_chart_script,
        'line_chart_div': line_chart_div,
        'pie_chart_script': pie_chart_script,
        'pie_chart_div': pie_chart_div,
        'bokeh_js': bokeh_js,
        'bokeh_css': bokeh_css
    })

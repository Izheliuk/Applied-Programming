from django import forms
from myapp.models import Client, RepairProject, Task, Worker

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']

class RepairProjectForm(forms.ModelForm):
    class Meta:
        model = RepairProject
        fields = ['project_name', 'work_description', 'start_date', 'end_date', 'client']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_description', 'completion_date', 'status', 'project', 'worker']

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'position']

from rest_framework import serializers
from .models import Client, RepairProject, Task, Worker

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class RepairProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairProject
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'



class RepairProject(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    work_description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'repair_project'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_description = models.TextField()
    completion_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=11)
    project = models.ForeignKey(RepairProject, models.DO_NOTHING)
    worker = models.ForeignKey('Worker', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task'


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'worker'

from django.contrib import admin
from .models import Client, Task, Worker, RepairProject


admin.site.register(Client)
admin.site.register(RepairProject)
admin.site.register(Worker)
admin.site.register(Task)

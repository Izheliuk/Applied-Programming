from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import ClientViewSet, RepairProjectViewSet, TaskViewSet, WorkerViewSet, ProjectReportView

router = DefaultRouter()
router.register(r'clients', ClientViewSet)         
router.register(r'repair_projects', RepairProjectViewSet)  
router.register(r'tasks', TaskViewSet)               
router.register(r'workers', WorkerViewSet)         

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),  
    path('', include('myapp.urls')),

    path('reports/project/', ProjectReportView.as_view(), name='project_report'), 
]



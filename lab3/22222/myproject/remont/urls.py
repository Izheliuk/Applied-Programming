from django.urls import path
from . import views

urlpatterns = [
    # Client URLs
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),

    # Repair Project URLs
    path('repair_projects/', views.repair_project_list, name='repair_project_list'),
    path('repair_projects/create/', views.repair_project_create, name='repair_project_create'),
    path('repair_projects/<int:pk>/edit/', views.repair_project_edit, name='repair_project_edit'),
    path('repair_projects/<int:pk>/delete/', views.repair_project_delete, name='repair_project_delete'),

    # Service Category URLs
    path('service_categories/', views.service_category_list, name='service_category_list'),
    path('service_categories/create/', views.service_category_create, name='service_category_create'),
    path('service_categories/<int:pk>/edit/', views.service_category_edit, name='service_category_edit'),
    path('service_categories/<int:pk>/delete/', views.service_category_delete, name='service_category_delete'),

    # Service URLs
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # Worker URLs
    path('workers/', views.worker_list, name='worker_list'),
    path('workers/create/', views.worker_create, name='worker_create'),
    path('workers/<int:pk>/edit/', views.worker_edit, name='worker_edit'),
    path('workers/<int:pk>/delete/', views.worker_delete, name='worker_delete'),

    # Task URLs
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

    # Supplier URLs
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/edit/', views.supplier_edit, name='supplier_edit'),
    path('suppliers/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),

    # Material URLs
    path('materials/', views.material_list, name='material_list'),
    path('materials/create/', views.material_create, name='material_create'),
    path('materials/<int:pk>/edit/', views.material_edit, name='material_edit'),
    path('materials/<int:pk>/delete/', views.material_delete, name='material_delete'),

    # Invoice URLs
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/create/', views.invoice_create, name='invoice_create'),
    path('invoices/<int:pk>/edit/', views.invoice_edit, name='invoice_edit'),
    path('invoices/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
]

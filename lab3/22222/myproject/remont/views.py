from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientForm, RepairProjectForm, ServiceCategoryForm, ServiceForm, WorkerForm, TaskForm, SupplierForm, MaterialForm, InvoiceForm
from .repository import ClientRepository, RepairProjectRepository, ServiceCategoryRepository, ServiceRepository, WorkerRepository, TaskRepository, SupplierRepository, MaterialRepository, InvoiceRepository

# Client Views
def client_list(request):
    clients = ClientRepository.get_all_clients()
    return render(request, 'client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ClientRepository.create_client(data)
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_edit(request, pk):
    client = ClientRepository.get_client_by_id(pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            data = form.cleaned_data
            ClientRepository.update_client(pk, data)
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, pk):
    ClientRepository.delete_client(pk)
    return redirect('client_list')


# Repair Project Views
def repair_project_list(request):
    repair_projects = RepairProjectRepository.get_all_repair_projects()
    return render(request, 'repair_project_list.html', {'repair_projects': repair_projects})

def repair_project_create(request):
    if request.method == 'POST':
        form = RepairProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RepairProjectRepository.create_repair_project(data)
            return redirect('repair_project_list')
    else:
        form = RepairProjectForm()
    return render(request, 'repair_project_form.html', {'form': form})

def repair_project_edit(request, pk):
    project = RepairProjectRepository.get_repair_project_by_id(pk)
    if request.method == 'POST':
        form = RepairProjectForm(request.POST, instance=project)
        if form.is_valid():
            data = form.cleaned_data
            RepairProjectRepository.update_repair_project(pk, data)
            return redirect('repair_project_list')
    else:
        form = RepairProjectForm(instance=project)
    return render(request, 'repair_project_form.html', {'form': form})

def repair_project_delete(request, pk):
    RepairProjectRepository.delete_repair_project(pk)
    return redirect('repair_project_list')


# Service Category Views
def service_category_list(request):
    categories = ServiceCategoryRepository.get_all_service_categories()
    return render(request, 'service_category_list.html', {'categories': categories})

def service_category_create(request):
    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ServiceCategoryRepository.create_service_category(data)
            return redirect('service_category_list')
    else:
        form = ServiceCategoryForm()
    return render(request, 'service_category_form.html', {'form': form})

def service_category_edit(request, pk):
    category = ServiceCategoryRepository.get_service_category_by_id(pk)
    if request.method == 'POST':
        form = ServiceCategoryForm(request.POST, instance=category)
        if form.is_valid():
            data = form.cleaned_data
            ServiceCategoryRepository.update_service_category(pk, data)
            return redirect('service_category_list')
    else:
        form = ServiceCategoryForm(instance=category)
    return render(request, 'service_category_form.html', {'form': form})

def service_category_delete(request, pk):
    ServiceCategoryRepository.delete_service_category(pk)
    return redirect('service_category_list')


# Service Views
def service_list(request):
    services = ServiceRepository.get_all_services()
    return render(request, 'service_list.html', {'services': services})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ServiceRepository.create_service(data)
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service_form.html', {'form': form})

def service_edit(request, pk):
    service = ServiceRepository.get_service_by_id(pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            data = form.cleaned_data
            ServiceRepository.update_service(pk, data)
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_form.html', {'form': form})

def service_delete(request, pk):
    ServiceRepository.delete_service(pk)
    return redirect('service_list')


# Worker Views
def worker_list(request):
    workers = WorkerRepository.get_all_workers()
    return render(request, 'worker_list.html', {'workers': workers})

def worker_create(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            WorkerRepository.create_worker(data)
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'worker_form.html', {'form': form})

def worker_edit(request, pk):
    worker = WorkerRepository.get_worker_by_id(pk)
    if request.method == 'POST':
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            data = form.cleaned_data
            WorkerRepository.update_worker(pk, data)
            return redirect('worker_list')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'worker_form.html', {'form': form})

def worker_delete(request, pk):
    WorkerRepository.delete_worker(pk)
    return redirect('worker_list')


# Task Views
def task_list(request):
    tasks = TaskRepository.get_all_tasks()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TaskRepository.create_task(data)
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_edit(request, pk):
    task = TaskRepository.get_task_by_id(pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            data = form.cleaned_data
            TaskRepository.update_task(pk, data)
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    TaskRepository.delete_task(pk)
    return redirect('task_list')


# Supplier Views
def supplier_list(request):
    suppliers = SupplierRepository.get_all_suppliers()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            SupplierRepository.create_supplier(data)
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'supplier_form.html', {'form': form})

def supplier_edit(request, pk):
    supplier = SupplierRepository.get_supplier_by_id(pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            data = form.cleaned_data
            SupplierRepository.update_supplier(pk, data)
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'supplier_form.html', {'form': form})

def supplier_delete(request, pk):
    SupplierRepository.delete_supplier(pk)
    return redirect('supplier_list')


# Material Views
def material_list(request):
    materials = MaterialRepository.get_all_materials()
    return render(request, 'material_list.html', {'materials': materials})

def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MaterialRepository.create_material(data)
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'material_form.html', {'form': form})

def material_edit(request, pk):
    material = MaterialRepository.get_material_by_id(pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            data = form.cleaned_data
            MaterialRepository.update_material(pk, data)
            return redirect('material_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'material_form.html', {'form': form})

def material_delete(request, pk):
    MaterialRepository.delete_material(pk)
    return redirect('material_list')


# Invoice Views
def invoice_list(request):
    invoices = InvoiceRepository.get_all_invoices()
    return render(request, 'invoice_list.html', {'invoices': invoices})

def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            InvoiceRepository.create_invoice(data)
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoice_form.html', {'form': form})

def invoice_edit(request, pk):
    invoice = InvoiceRepository.get_invoice_by_id(pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            data = form.cleaned_data
            InvoiceRepository.update_invoice(pk, data)
            return redirect('invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoice_form.html', {'form': form})

def invoice_delete(request, pk):
    InvoiceRepository.delete_invoice(pk)
    return redirect('invoice_list')

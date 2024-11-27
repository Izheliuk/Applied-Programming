from django import forms
from .models import Client, RepairProject, ServiceCategory, Service, Worker, Task, Supplier, Material, Invoice

# Form for Client
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']

# Form for Repair Project
class RepairProjectForm(forms.ModelForm):
    class Meta:
        model = RepairProject
        fields = ['project_name', 'work_description', 'start_date', 'end_date', 'status', 'budget', 'client']

# Form for Service Category
class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['category_name', 'category_description']

# Form for Service
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'service_description', 'price_per_unit', 'category']

# Form for Worker
class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'phone_number', 'position', 'qualification']

# Form for Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_description', 'completion_date', 'status', 'project', 'worker', 'service']

# Form for Supplier
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['company_name', 'contact_person', 'phone_number', 'address', 'email']

# Form for Material
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['material_name', 'material_type', 'quantity_in_stock', 'price_per_unit', 'supplier']

# Form for Invoice
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['project', 'invoice_date', 'amount', 'payment_status']

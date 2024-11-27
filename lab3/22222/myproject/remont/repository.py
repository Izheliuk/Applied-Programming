from .models import Client, RepairProject, ServiceCategory, Service, Worker, Task, Supplier, Material, Invoice

# Repository for Client
class ClientRepository:
    @staticmethod
    def get_all_clients():
        return Client.objects.all()

    @staticmethod
    def get_client_by_id(client_id):
        return Client.objects.get(id=client_id)

    @staticmethod
    def create_client(data):
        client = Client.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
            email=data.get('email', ''),
            address=data['address']
        )
        return client

    @staticmethod
    def update_client(client_id, data):
        client = Client.objects.get(id=client_id)
        client.first_name = data.get('first_name', client.first_name)
        client.last_name = data.get('last_name', client.last_name)
        client.phone_number = data.get('phone_number', client.phone_number)
        client.email = data.get('email', client.email)
        client.address = data.get('address', client.address)
        client.save()
        return client

    @staticmethod
    def delete_client(client_id):
        client = Client.objects.get(id=client_id)
        client.delete()

# Repository for RepairProject
class RepairProjectRepository:
    @staticmethod
    def get_all_repair_projects():
        return RepairProject.objects.all()

    @staticmethod
    def get_repair_project_by_id(project_id):
        return RepairProject.objects.get(id=project_id)

    @staticmethod
    def create_repair_project(data):
        project = RepairProject.objects.create(
            project_name=data['project_name'],
            work_description=data['work_description'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            status=data.get('status', 'Pending'),
            budget=data['budget'],
            client_id=data['client_id']
        )
        return project

    @staticmethod
    def update_repair_project(project_id, data):
        project = RepairProject.objects.get(id=project_id)
        project.project_name = data.get('project_name', project.project_name)
        project.work_description = data.get('work_description', project.work_description)
        project.start_date = data.get('start_date', project.start_date)
        project.end_date = data.get('end_date', project.end_date)
        project.status = data.get('status', project.status)
        project.budget = data.get('budget', project.budget)
        project.client_id = data.get('client_id', project.client_id)
        project.save()
        return project

    @staticmethod
    def delete_repair_project(project_id):
        project = RepairProject.objects.get(id=project_id)
        project.delete()

# Repository for ServiceCategory
class ServiceCategoryRepository:
    @staticmethod
    def get_all_service_categories():
        return ServiceCategory.objects.all()

    @staticmethod
    def get_service_category_by_id(category_id):
        return ServiceCategory.objects.get(id=category_id)

    @staticmethod
    def create_service_category(data):
        category = ServiceCategory.objects.create(
            category_name=data['category_name'],
            category_description=data['category_description']
        )
        return category

    @staticmethod
    def update_service_category(category_id, data):
        category = ServiceCategory.objects.get(id=category_id)
        category.category_name = data.get('category_name', category.category_name)
        category.category_description = data.get('category_description', category.category_description)
        category.save()
        return category

    @staticmethod
    def delete_service_category(category_id):
        category = ServiceCategory.objects.get(id=category_id)
        category.delete()

# Repository for Service
class ServiceRepository:
    @staticmethod
    def get_all_services():
        return Service.objects.all()

    @staticmethod
    def get_service_by_id(service_id):
        return Service.objects.get(id=service_id)

    @staticmethod
    def create_service(data):
        service = Service.objects.create(
            service_name=data['service_name'],
            service_description=data['service_description'],
            price_per_unit=data['price_per_unit'],
            category_id=data['category_id']
        )
        return service

    @staticmethod
    def update_service(service_id, data):
        service = Service.objects.get(id=service_id)
        service.service_name = data.get('service_name', service.service_name)
        service.service_description = data.get('service_description', service.service_description)
        service.price_per_unit = data.get('price_per_unit', service.price_per_unit)
        service.category_id = data.get('category_id', service.category_id)
        service.save()
        return service

    @staticmethod
    def delete_service(service_id):
        service = Service.objects.get(id=service_id)
        service.delete()

# Repository for Worker
class WorkerRepository:
    @staticmethod
    def get_all_workers():
        return Worker.objects.all()

    @staticmethod
    def get_worker_by_id(worker_id):
        return Worker.objects.get(id=worker_id)

    @staticmethod
    def create_worker(data):
        worker = Worker.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
            position=data['position'],
            qualification=data['qualification']
        )
        return worker

    @staticmethod
    def update_worker(worker_id, data):
        worker = Worker.objects.get(id=worker_id)
        worker.first_name = data.get('first_name', worker.first_name)
        worker.last_name = data.get('last_name', worker.last_name)
        worker.phone_number = data.get('phone_number', worker.phone_number)
        worker.position = data.get('position', worker.position)
        worker.qualification = data.get('qualification', worker.qualification)
        worker.save()
        return worker

    @staticmethod
    def delete_worker(worker_id):
        worker = Worker.objects.get(id=worker_id)
        worker.delete()

# Repository for Task
class TaskRepository:
    @staticmethod
    def get_all_tasks():
        return Task.objects.all()

    @staticmethod
    def get_task_by_id(task_id):
        return Task.objects.get(id=task_id)

    @staticmethod
    def create_task(data):
        task = Task.objects.create(
            task_description=data['task_description'],
            completion_date=data['completion_date'],
            status=data['status'],
            project_id=data['project_id'],
            worker_id=data['worker_id'],
            service_id=data['service_id']
        )
        return task

    @staticmethod
    def update_task(task_id, data):
        task = Task.objects.get(id=task_id)
        task.task_description = data.get('task_description', task.task_description)
        task.completion_date = data.get('completion_date', task.completion_date)
        task.status = data.get('status', task.status)
        task.project_id = data.get('project_id', task.project_id)
        task.worker_id = data.get('worker_id', task.worker_id)
        task.service_id = data.get('service_id', task.service_id)
        task.save()
        return task

    @staticmethod
    def delete_task(task_id):
        task = Task.objects.get(id=task_id)
        task.delete()

# Repository for Supplier
class SupplierRepository:
    @staticmethod
    def get_all_suppliers():
        return Supplier.objects.all()

    @staticmethod
    def get_supplier_by_id(supplier_id):
        return Supplier.objects.get(id=supplier_id)

    @staticmethod
    def create_supplier(data):
        supplier = Supplier.objects.create(
            company_name=data['company_name'],
            contact_person=data['contact_person'],
            phone_number=data['phone_number'],
            address=data['address'],
            email=data['email']
        )
        return supplier

    @staticmethod
    def update_supplier(supplier_id, data):
        supplier = Supplier.objects.get(id=supplier_id)
        supplier.company_name = data.get('company_name', supplier.company_name)
        supplier.contact_person = data.get('contact_person', supplier.contact_person)
        supplier.phone_number = data.get('phone_number', supplier.phone_number)
        supplier.address = data.get('address', supplier.address)
        supplier.email = data.get('email', supplier.email)
        supplier.save()
        return supplier

    @staticmethod
    def delete_supplier(supplier_id):
        supplier = Supplier.objects.get(id=supplier_id)
        supplier.delete()

# Repository for Material
class MaterialRepository:
    @staticmethod
    def get_all_materials():
        return Material.objects.all()

    @staticmethod
    def get_material_by_id(material_id):
        return Material.objects.get(id=material_id)

    @staticmethod
    def create_material(data):
        material = Material.objects.create(
            material_name=data['material_name'],
            type=data['type'],
            quantity_in_stock=data['quantity_in_stock'],
            price_per_unit=data['price_per_unit'],
            supplier_id=data['supplier_id']
        )
        return material

    @staticmethod
    def update_material(material_id, data):
        material = Material.objects.get(id=material_id)
        material.material_name = data.get('material_name', material.material_name)
        material.type = data.get('type', material.type)
        material.quantity_in_stock = data.get('quantity_in_stock', material.quantity_in_stock)
        material.price_per_unit = data.get('price_per_unit', material.price_per_unit)
        material.supplier_id = data.get('supplier_id', material.supplier_id)
        material.save()
        return material

    @staticmethod
    def delete_material(material_id):
        material = Material.objects.get(id=material_id)
        material.delete()

# Repository for Invoice
class InvoiceRepository:
    @staticmethod
    def get_all_invoices():
        return Invoice.objects.all()

    @staticmethod
    def get_invoice_by_id(invoice_id):
        return Invoice.objects.get(id=invoice_id)

    @staticmethod
    def create_invoice(data):
        invoice = Invoice.objects.create(
            project_id=data['project_id'],
            invoice_date=data['invoice_date'],
            amount=data['amount'],
            payment_status=data['payment_status']
        )
        return invoice

    @staticmethod
    def update_invoice(invoice_id, data):
        invoice = Invoice.objects.get(id=invoice_id)
        invoice.project_id = data.get('project_id', invoice.project_id)
        invoice.invoice_date = data.get('invoice_date', invoice.invoice_date)
        invoice.amount = data.get('amount', invoice.amount)
        invoice.payment_status = data.get('payment_status', invoice.payment_status)
        invoice.save()
        return invoice

    @staticmethod
    def delete_invoice(invoice_id):
        invoice = Invoice.objects.get(id=invoice_id)
        invoice.delete()

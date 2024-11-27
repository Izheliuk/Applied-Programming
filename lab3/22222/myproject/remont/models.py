from django.db import models

# Client Model
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.TextField()

    class Meta:
        db_table = 'remont_client'  # If you have a custom table name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Repair Project Model
class RepairProject(models.Model):
    project_name = models.CharField(max_length=100)
    work_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

# Service Category Model
class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

# Service Model
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name

# Worker Model
class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Task Model
class Task(models.Model):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (NOT_STARTED, 'Not Started'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    task_description = models.TextField()
    completion_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    project = models.ForeignKey(RepairProject, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_description

# Supplier Model
class Supplier(models.Model):
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.company_name

# Material Model
class Material(models.Model):
    material_name = models.CharField(max_length=100)
    material_type = models.CharField(max_length=50)
    quantity_in_stock = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.material_name

# Invoice Model
class Invoice(models.Model):
    PENDING = 'Pending'
    PAID = 'Paid'
    OVERDUE = 'Overdue'
    PAYMENT_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (OVERDUE, 'Overdue'),
    ]

    project = models.ForeignKey(RepairProject, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Invoice for {self.project.project_name}"

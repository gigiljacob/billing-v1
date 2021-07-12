from django.db import models


class Category(models.Model):
    """
    Service categories model
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    level = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Service(models.Model):
    """
    Service model holds all the services, and a relation to it's corresponding category
    from the category model.
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    All the employee details would be stored in this model. If required can attach
    to a bill for future reference.
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    skill_set = models.ManyToManyField(Service, blank=True, related_name="Service")
    address = models.TextField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    """
    Customer model holds details about the customer, and their issues
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    issue = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return self.name


class AssignedWork(models.Model):
    """
    Assign new work for employee from customer pool.
    """
    current_status = (
        ('1', 'Assigned'), ('2', 'In Progress'), ('3', 'On Hold'), ('0', 'Completed'),
        ('-1', 'Layoff')
    )

    customer = models.ForeignKey(Customer, models.CASCADE)
    employee = models.ForeignKey(Employee, models.CASCADE)
    status = models.CharField(choices=current_status, max_length=15)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self):
        return str(self.customer)

# class Bill(models.Model):
#     """
#     Newly generated bill would be saved in this model.
#     """
#     number = models.CharField(max_length=20, null=False, blank=False)
#     customer = models.ForeignKey(Customer, models.CASCADE)
#     employee = models.ForeignKey(Employee, models.CASCADE)
#     estimate = models.FileField(upload_to='bill')
#     created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
#     updated_at = models.DateTimeField(auto_created=True, auto_now=True)


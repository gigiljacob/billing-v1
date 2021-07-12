from django.contrib import admin

from crm.models import Category, Service, Employee, Customer, AssignedWork

admin.site.register(Category)
admin.site.register(Service)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'skills', 'created_at', 'updated_at']

    def skills(self, obj):
        return ", ".join([skill.name for skill in obj.skill_set.all()])


admin.site.register(Employee, EmployeeAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


admin.site.register(Customer, CustomerAdmin)


class AssignedWorkAdmin(admin.ModelAdmin):
    list_display = ['customer', 'employee', 'status', 'created_at', 'updated_at']


admin.site.register(AssignedWork, AssignedWorkAdmin)

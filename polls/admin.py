from django.contrib import admin
from polls.models import Employee

# Register your models here.

class Employee_admin(admin.ModelAdmin):
	l = ['emp_name','emp_salary','emp_city']

admin.site.register(Employee,Employee_admin)

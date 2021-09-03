from django.db import models

# Create your models here.
class Employee(models.Model):
	emp_name = models.CharField(max_length=20)
	emp_salary = models.IntegerField(null=True)
	emp_city = models.CharField(max_length=50)

	def __str__(self):
		return self.emp_name


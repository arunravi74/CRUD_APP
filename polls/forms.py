from django import forms
from django.contrib.auth.forms import UserCreationForm
from polls.models import Employee
from django.contrib.auth.models import User

class Employeeforms(forms.ModelForm):
	class Meta:
		model = Employee
		fields = '__all__'#['emp_name','emp_salary','emp_city']

class RegisterForms(UserCreationForm):
	Email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','Email','password1','password2']
from django.shortcuts import render,redirect
from polls.models import Employee
from polls.forms import Employeeforms,RegisterForms


def show_employee(request):
	emplist = Employee.objects.all()
	return render(request,'index.html',{'emplist':emplist})

def create_employee(request):
	form = Employeeforms()
	if request.method == 'POST':
		form = Employeeforms(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")

	return render(request,'form.html',{'form':form})

def remove_employee(request,id):
	remove = Employee.objects.get(id = id)
	remove.delete()
	return redirect('/')


def edit_employee(request,id):
	employee = Employee.objects.get(id = id) 
	form = Employeeforms(instance=employee)
	if request.method == 'POST':
		form = Employeeforms(request.POST,instance = employee)	
		if form.is_valid():
			form.save()
			return redirect("/")

	return render(request,'edit.html',{'form':form})





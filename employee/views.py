from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm

def home(request):
    return HttpResponse("Hello, welcome to the Employee Project!")

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form': form})

def success(request):
    return render(request, 'employee/success.html')


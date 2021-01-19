from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def home(request):
    return render(request,'crud/home.html')

def employees(request):
    employees = Employee.objects.all()
    return render(request,'crud/employees.html',{'employees':employees})

def create(request):
    if request.method == 'GET':
        return render(request,'crud/create.html',{'form': EmployeeForm})
    else:
        try:
            form = EmployeeForm(request.POST)
            form.save()
            return redirect('employees')
        except ValueError:
            return render(request,'crud/create.html',{'form': EmployeeForm, 'error': 'Bad data entered, please enter valid data'})

def viewemployee(request, employee_pk):
    employee = get_object_or_404(Employee,pk=employee_pk)
    if request.method == 'GET':
        form = EmployeeForm(instance=employee)
        return render(request, 'crud/viewemployee.html', {'employee': employee,'form': form})
    else:
        try:
            form = EmployeeForm(request.POST, instance=employee)
            form.save()
            return redirect('employees')
        except ValueError:
            return render(request, 'crud/viewemployee.html',{'employee':employee, 'form':form, 'error':'Bad data, refill data!' })

def deleteemployee(request, employee_pk):
    employee = get_object_or_404(Employee, pk=employee_pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees') 
     
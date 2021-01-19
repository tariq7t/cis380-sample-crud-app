from django.forms import ModelForm
from .models import Employee

# We are creating our own form for creating an employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','phone']
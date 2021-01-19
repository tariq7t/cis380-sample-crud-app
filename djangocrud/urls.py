
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('employees/',views.employees, name='employees'),
    path('create/',views.create, name='create'),
    path('employee/<int:employee_pk>',views.viewemployee, name='viewemployee'),
    path('employee/<int:employee_pk>/delete',views.deleteemployee, name='deleteemployee'),




]

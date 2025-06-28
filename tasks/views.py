from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
from tasks.models import Employee, Task, TaskDetail, Project

# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    context = {
        'names': ['Alice', 'Bob', 'John'],
        'age': [23, 35, 45],
    }
    return render(request, 'test.html', context)

def create_task(request):
    employees = Employee.objects.all()
    form = TaskForm(employees=employees)
    context = {"form": form}
    return render(request, 'task_form.html', context)  


def view_task(request):
    # retrive all data from task model
    task = Task.objects.all()

    #retrive a specific task
    # task_3 = Task.objects.get(id = 3)

    return render(request, 'show_task.html', {"tasks" : task, "task3" : task_3})
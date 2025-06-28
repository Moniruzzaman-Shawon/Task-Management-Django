from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date 
from django.db.models import Q, Count, Max, Min, Avg

# Create your views here.

def manager_dashboard(request):
    tasks = Task.objects.all()

    # getting task count 
    total_task = tasks.count()
    completed_task = Task.objects.filter(status = "COMPLETED").count()
    in_progress_task = Task.objects.filter(status = "IN_PROGRESS").count
    pending_task = Task .objects.filter(status = "PENDING").count
    
    context = {
        "tasks" : tasks,
        "total_task" : total_task,
        "pending_task" : pending_task,
        "in_progress_task" : in_progress_task,
        "completed_task" : completed_task
    }

    return render(request, "dashboard/manager-dashboard.html", context)

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
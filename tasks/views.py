from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def manager_dashboard(request):
    return render (request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render (request, "dashboard/user-dashboard.html")

def test(request):
    context = {
         'names' : ['Alice', 'Bob', 'John'],
         'age' : [23,35,45],
    }
    return render (request, 'test.html', context)
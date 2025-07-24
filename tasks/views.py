from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
from django.contrib import messages
from users.views import is_admin
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.contrib import messages
from .forms import TaskModelForm, TaskDetailModelForm
from django.utils.decorators import method_decorator




# Create your views here.

def is_manager(user):
    return user.groups.filter(name='Manager').exists()


def is_employee(user):
    return user.groups.filter(name='Manager').exists()

def manager_dashboard(request):

    # getting task count
    # total_task = tasks.count()
    # completed_task = Task.objects.filter(status="COMPLETED").count()
    # in_progress_task = Task.objects.filter(status='IN_PROGRESS').count()
    # pending_task = Task.objects.filter(status="PENDING").count()

    # count = {
    #     "total_task":
    #     "completed_task":
    #     "in_progress_task":
    #     "pending_task":
    # }
    type = request.GET.get('type', 'all')
    # print(type)

    counts = Task.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='COMPLETED')),
        in_progress=Count('id', filter=Q(status='IN_PROGRESS')),
        pending=Count('id', filter=Q(status='PENDING')),
    )
    # print("DEBUG - counts:", counts) 

    # Retriving task data

    base_query = Task.objects.select_related(
        'details').prefetch_related('assigned_to')

    if type == 'completed':
        tasks = base_query.filter(status='COMPLETED')
    elif type == 'in-progress':
        tasks = base_query.filter(status='IN_PROGRESS')
    elif type == 'pending':
        tasks = base_query.filter(status='PENDING')
    elif type == 'all':
        tasks = base_query.all()

    context = {
        "tasks": tasks,
        "counts": counts,
    }
    return render(request, "dashboard/manager-dashboard.html", context)


def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")


def test(request):
    names = ["Mahmud", "Ahamed", "John", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names": names,
        "age": 23,
        "count": count
    }
    return render(request, 'test.html', context)


class CreateTaskView(View):
    def get(self, request):
        task_form = TaskModelForm()
        task_detail_form = TaskDetailModelForm()
        context = {
            "task_form": task_form,
            "task_detail_form": task_detail_form,
        }
        return render(request, "task_form.html", context)

    def post(self, request):
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Created Successfully")
            return redirect('create-task')

        context = {
            "task_form": task_form,
            "task_detail_form": task_detail_form,
        }
        return render(request, "task_form.html", context)

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required("tasks.change_task", login_url='no-permission'), name='dispatch')
class UpdateTaskView(View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        task_form = TaskModelForm(instance=task)
        task_detail_form = TaskDetailModelForm(instance=task.details) if task.details else TaskDetailModelForm()
        context = {
            "task_form": task_form,
            "task_detail_form": task_detail_form,
        }
        return render(request, "task_form.html", context)

    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(request.POST, instance=task.details)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', id=id)

        context = {
            "task_form": task_form,
            "task_detail_form": task_detail_form,
        }
        return render(request, "task_form.html", context)



class UpdateTask(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'task_form.html'
    context_object_name = 'task'
    pk_url_kwarg = 'id'
    permission_required = 'tasks.change_task'
    raise_exception = False  
    login_url = 'login'  #  login page
    permission_denied_message = "You do not have permission to edit this task."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_form'] = self.get_form()
        if hasattr(self.object, 'details') and self.object.details:
            context['task_detail_form'] = TaskDetailModelForm(
                instance=self.object.details)
        else:
            context['task_detail_form'] = TaskDetailModelForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        task_form = TaskModelForm(request.POST, instance=self.object)
        task_detail_form = TaskDetailModelForm(
            request.POST, request.FILES, instance=getattr(self.object, 'details', None))

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', self.object.id)

        return self.render_to_response(self.get_context_data(
            task_form=task_form,
            task_detail_form=task_detail_form
        ))



@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required("tasks.delete_task", login_url='no-permission'), name='dispatch')
class DeleteTaskView(View):
    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        messages.success(request, 'Task Deleted Successfully')
        return redirect('manager-dashboard')

    def get(self, request, id):
        messages.error(request, 'Something went wrong')
        return redirect('manager-dashboard')
    
@login_required
@permission_required("tasks.view_task", login_url='no-permission')
def view_task(request):
    projects = Project.objects.annotate(
        num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects": projects})


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required("tasks.view_task", login_url='no-permission'), name='dispatch')
class TaskDetailsView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        status_choices = Task.STATUS_CHOICES
        return render(request, 'task_details.html', {"task": task, "status_choices": status_choices})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        selected_status = request.POST.get('task_status')
        print(selected_status)
        task.status = selected_status
        task.save()
        return redirect('task-details', task_id=task.id)


@login_required
def dashboard(request):
    if is_manager(request.user):
        return redirect('manager-dashboard')
    elif is_employee(request.user):
        return redirect('user-dashboard')
    elif is_admin(request.user):
        return redirect('admin-dashboard')

    return redirect('no-permission')
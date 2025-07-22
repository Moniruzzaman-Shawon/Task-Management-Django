from django.contrib import admin
from tasks.models import Task, TaskDetail, Employee, Project
from users.models import UserProfile  # Replace with actual model location


# Register your models here.
admin.site.register(Task)
admin.site.register(TaskDetail)
admin.site.register(Employee)
admin.site.register(Project)


admin.site.register(UserProfile)

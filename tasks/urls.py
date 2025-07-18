from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, test, create_task, view_task, update_task, delete_task, task_details

urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('user-dashboard/', user_dashboard),
    path('test/', test),
    path('create-task/', create_task, name='create-task'),
    path('view_task/', view_task),
    path('tasks/<int:task_id>/details/', task_details, name='task-details'),
    path('update-task/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
]
from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, test,  view_task

from .views import CreateTaskView,UpdateTaskView,DeleteTaskView,TaskDetailsView


urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path('user-dashboard/', user_dashboard),
    path('test/', test),
    # path('create-task/', create_task, name='create-task'),
    path('view_task/', view_task),
    # path('tasks/<int:task_id>/details/', task_details, name='task-details'),
    # path('update-task/<int:id>/', update_task, name='update-task'),
    path('update-task/<int:id>/', UpdateTaskView.as_view(), name='update-task'),

    # path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('create-task/', CreateTaskView.as_view(), name='create-task'),
    path('delete-task/<int:id>/', DeleteTaskView.as_view(), name='delete-task'),
    path('task-details/<int:task_id>/', TaskDetailsView.as_view(), name='task-details'),

]
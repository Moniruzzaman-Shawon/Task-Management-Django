from django.urls import path
from users.views import sign_up, sign_in, sign_out, admin_dashboard, assign_role, create_group, group_list, EditProfileView, ProfileView

urlpatterns = [
    path('sign-up/', sign_up, name='sign-up'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-out/', sign_out, name='logout'),
    path('admin/dashboard/', admin_dashboard, name="admin-dashboard"),
    path('admin/<int:user_id>/assign-role/', assign_role, name="assign-role"),
    path('admin/create-group/', create_group, name="create-group"),
    path('admin/group-list/', group_list, name='group-list'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(),name='edit_profile')
]
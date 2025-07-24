from django.urls import path
from users.views import  admin_dashboard,   group_list, EditProfileView, ProfileView
from .views import SignUpView, SignInView, SignOutView,CreateGroupView,AssignRoleView

urlpatterns = [
    # path('sign-up/', sign_up, name='sign-up'),
    # path('sign-in/', sign_in, name='sign-in'),
    # path('sign-out/', sign_out, name='logout'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('admin/dashboard/', admin_dashboard, name="admin-dashboard"),
    # path('admin/<int:user_id>/assign-role/', assign_role, name="assign-role"),
    # path('admin/create-group/', create_group, name="create-group"),
    path('admin/group-list/', group_list, name='group-list'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(),name='edit_profile'),
    path('create-group/', CreateGroupView.as_view(), name='create-group'),
    path('assign-role/<int:user_id>/', AssignRoleView.as_view(), name='assign-role'),

]
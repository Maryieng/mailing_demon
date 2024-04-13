from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserPasswordRecoveryView, ProfileView, activate_user, toggle_activity, \
    ManagerListView

app_name = UsersConfig.name


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('recovery_password', UserPasswordRecoveryView.as_view(), name="recovery_password"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/', activate_user),
    path('manager/', ManagerListView.as_view(), name='manager_list'),
    path('activity/<int:pk>/', toggle_activity, name='manager')
    ]
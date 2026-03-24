from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from uem_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Devices
    path('devices/', views.device_list, name='device_list'),
    path('devices/add/', views.device_add, name='device_add'),
    path('devices/<int:pk>/', views.device_detail, name='device_detail'),
    path('devices/<int:pk>/delete/', views.device_delete, name='device_delete'),

    # Policies
    path('policies/', views.policy_list, name='policy_list'),
    path('policies/add/', views.policy_add, name='policy_add'),
    path('policies/<int:pk>/delete/', views.policy_delete, name='policy_delete'),

    # FileVault
    path('filevault/', views.filevault, name='filevault'),

    # Remote Access
    path('remote-access/', views.remote_access, name='remote_access'),

    # Groups
    path('groups/', views.group_list, name='group_list'),
    path('groups/add/', views.group_add, name='group_add'),
    path('groups/<int:pk>/delete/', views.group_delete, name='group_delete'),
]

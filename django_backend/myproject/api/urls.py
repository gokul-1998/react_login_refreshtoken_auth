# api/urls.py
from django.urls import path
from .views import EmployeeListCreate, EmployeeDetail, UserList, UserDetail, handle_login, handle_logout, register_user

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('users/', UserList.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('auth', handle_login, name='login'),
    path('auth/logout/', handle_logout, name='logout'),
    path('register', register_user, name='register_user'),
]

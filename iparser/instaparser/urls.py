from django.urls import path

from instaparser.views.parse import Task, Home
from instaparser.views.auth import user_logout, Register, UserLogin

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('task/<int:task_id>/', Task.as_view(), name='task'),
]

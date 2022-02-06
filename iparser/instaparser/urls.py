from django.urls import path

from instaparser.views import index, register, user_login, user_logout, task

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('task/<int:task_id>/', task, name='task'),
]

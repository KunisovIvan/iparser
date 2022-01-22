from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from instaparser.form import UsernameForm

from instaparser.models import TaskForParse


def index(request):
    """Основная функция, для ренда шаблона"""

    user = request.user

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':

        form_username = UsernameForm(data=request.POST)

        if form_username.is_valid():
            user_to_scrape = form_username.cleaned_data['username'].lower()
            TaskForParse.objects.create(
                user=user,
                user_to_scrape=user_to_scrape,
            )
            return redirect('home')
    else:
        form_username = UsernameForm()
        task_for_parse = TaskForParse.objects.filter(user=user)
        file_list = {}
        data = None

        if task_for_parse:
            file_list = {x: x.file.name[16:] for x in task_for_parse}
            print('file_list-> ', file_list)

            task_latest = task_for_parse.latest('created_at')
            if task_latest:
                data = task_latest.data_from_parse.all().order_by('-pk')
                print('data-> ', data)

    return render(request, 'instaparser/index.html',
                  {
                      'form_username': form_username,
                      'file_list': file_list,
                      'data': data,
                   })


def register(request):
    """Отвечает за логику регистрации пользователя."""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserCreationForm()
    return render(request, 'instaparser/register.html', {'form': form, 'title': 'Регистрация'})


def user_login(request):
    """Отвечает за логику авторизации пользователя."""

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'instaparser/login.html', {'form': form})


def user_logout(request):
    """Отвечает за логику разлогирования пользователя."""

    logout(request)
    return redirect('login')

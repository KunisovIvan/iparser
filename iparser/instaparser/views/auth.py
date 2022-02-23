from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View


class Register(View):
    """Отвечает за логику регистрации пользователя."""

    template_name = 'instaparser/register.html'
    form_class = UserCreationForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации!')
        return render(request, self.template_name, {'form': form})


class UserLogin(View):
    """Отвечает за логику авторизации пользователя."""

    template_name = 'instaparser/login.html'
    form_class = AuthenticationForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})


def user_logout(request):
    """Отвечает за логику разлогирования пользователя."""

    logout(request)
    return redirect('login')

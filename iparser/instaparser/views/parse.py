from typing import Optional

from django.shortcuts import render, redirect
from django.views import View

from instaparser.form import HomeForm

from instaparser.models import TaskForParse


class Home(View):
    """Отвечает за работу с данными на главной странице."""

    template_name = 'instaparser/index.html'
    form = HomeForm

    def get(self, request, task_id: Optional[int] = None):
        if not request.user.is_authenticated:
            return redirect('login')
        user = request.user
        form = self.form
        task_for_parse = TaskForParse.objects.filter(user=user)
        task_to_file_name_dict = {}
        data = None
        if task_for_parse:
            # Собираем словарь, где ключ задача на парсинг, а значение имя файла данной задачи
            task_to_file_name_dict = {x: x.file.name[5:] for x in task_for_parse}
            # Получаем последнюю по дате создания задачу и выводим спаршенные для нее данные
            task = task_for_parse.all().latest('created_at')
            if task:
                data = task.data_from_parse.all().order_by('-pk')

        return render(request, self.template_name, {'form': form,
                                                    'task_to_file_name_dict': task_to_file_name_dict,
                                                    'data': data})

    def post(self, request):
        user = request.user
        form = self.form(data=request.POST)
        if form.is_valid():
            user_to_scrape = form.cleaned_data['username'].lower()
            type_of_parse = form.cleaned_data['type_of_parse'].lower()
            is_parse_new_data = form.cleaned_data['is_parse_new_data'].lower()
            task_for_parse, is_created = TaskForParse.objects.get_or_create(user=user,
                                                                            user_to_scrape=user_to_scrape)
            if not is_created:
                task_for_parse.status = TaskForParse.Status.WAITING
                task_for_parse.file = None
                task_for_parse.save()
                if is_parse_new_data == '2':
                    task_for_parse.data_from_parse.all().delete()
            if type_of_parse == '1':
                task_for_parse.type_of_parse = TaskForParse.TypeOfParse.FOLLOWERS
                task_for_parse.save()
            else:
                task_for_parse.type_of_parse = TaskForParse.TypeOfParse.FOLLOWING
                task_for_parse.save()
            return redirect('home')
        return redirect('home')


class Task(Home):
    """Отвечает за работу с данными на странице с конкретной задачей."""

    def get(self, request, task_id: Optional[int] = None):
        if not request.user.is_authenticated:
            return redirect('login')
        user = request.user
        form = self.form
        task_for_parse = TaskForParse.objects.filter(user=user)
        task_to_file_name_dict = {}
        data = None
        if task_for_parse:
            # Собираем словарь, где ключ задача на парсинг, а значение имя файла данной задачи
            task_to_file_name_dict = {x: x.file.name[5:] for x in task_for_parse}
            # Получаем необходимую для данной страницы задачу и выводим спаршенные для нее данные
            task = task_for_parse.filter(pk=task_id).first()
            if task:
                data = task.data_from_parse.all().order_by('-pk')

        return render(request, self.template_name, {'form': form,
                                                    'task_to_file_name_dict': task_to_file_name_dict,
                                                    'data': data})

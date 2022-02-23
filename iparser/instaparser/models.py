from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class TaskForParse(models.Model):
    """Модель задач на парсинг."""

    class Status(models.TextChoices):
        WAITING = 'waiting', 'Задача на проверке'
        IN_PROGRESS = 'in_progress', 'Задача выполняется'
        DONE = 'done', 'Задача выполнена'
        ERROR = 'error', 'Упс! Что-то пощло не так! Попробуйте перезапустить задачу'

    class TypeOfParse(models.TextChoices):
        FOLLOWERS = 'followers', 'Cбор подписчиков'
        FOLLOWING = 'following', 'Сбор подписок'

    user = models.ForeignKey(User, related_name='task_for_parse', verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    user_to_scrape = models.CharField(max_length=255, verbose_name='Аккаунт для парсинга')
    count_parse_data = models.PositiveIntegerField(verbose_name='Спаршено данных', blank=True, null=True, default=0)
    next_max_id = models.CharField(max_length=255, verbose_name='next_max_id', blank=True, null=True, default='')
    type_of_parse = models.CharField(max_length=20, choices=TypeOfParse.choices, default=TypeOfParse.FOLLOWERS,
                                     verbose_name='Тип сбора данных')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.WAITING,
                              verbose_name='Статус')
    file = models.FileField(verbose_name='', upload_to='file/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)

    def __str__(self):
        return f'{self.user}: {self.user_to_scrape}'

    class Meta:
        verbose_name = 'Задача на парсинг'
        verbose_name_plural = 'Задачи на парсинг'

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_id': self.pk})


class Data(models.Model):
    """Модель cпаршеных данных."""

    task_for_parse = models.ForeignKey(TaskForParse, related_name='data_from_parse', verbose_name='задача на парсинг',
                                       on_delete=models.CASCADE)
    username = models.CharField(max_length=255, verbose_name='Username', blank=True, null=True, default='')
    full_name = models.CharField(max_length=255, verbose_name='ФИО', blank=True, null=True, default='')
    biography = models.CharField(max_length=500, verbose_name='Описание профиля', blank=True, null=True, default='')
    is_private = models.BooleanField(verbose_name='Приватный ли аккаунт', blank=True, null=True, default=False)
    follower_count = models.PositiveIntegerField(verbose_name='Кол-во подписчиков', blank=True, null=True, default=0)
    following_count = models.PositiveIntegerField(verbose_name='Кол-во подписок', blank=True, null=True, default=0)
    following_tag_count = models.PositiveIntegerField(verbose_name='Кол-во подписок на теги', blank=True, null=True,
                                                      default=0)
    media_count = models.PositiveIntegerField(verbose_name='Кол-во публикаций', blank=True, null=True, default=0)
    usertags_count = models.PositiveIntegerField(verbose_name='Кол-во тегов пользователя', blank=True, null=True,
                                                 default=0)
    contact_phone_number = models.CharField(max_length=255, verbose_name='Телефон', blank=True, null=True, default='')
    public_email = models.CharField(max_length=255, verbose_name='Email', blank=True, null=True, default='')
    whatsapp_number = models.CharField(max_length=255, verbose_name='Whatsapp', blank=True, null=True, default='')
    business_contact_method = models.CharField(max_length=255, verbose_name='Способ связи', blank=True, null=True,
                                               default='')
    instagram_location_id = models.PositiveIntegerField(verbose_name='id геолокации', blank=True, null=True, default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Cпаршеные данные'
        verbose_name_plural = 'Cпаршеные данные'


class InstagramAccount(models.Model):
    """Модель аккаунтов instagram."""

    username = models.CharField(max_length=255, verbose_name='Username')
    enc_password = models.CharField(max_length=255, verbose_name='Хэш пароля')
    is_used = models.BooleanField(verbose_name='Отработал ли аккаунт', default=False)
    used_at = models.DateTimeField(verbose_name='Время последней работы аккаунта', default=timezone.now)


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Аккаунт instagram'
        verbose_name_plural = 'Аккаунты instagram'

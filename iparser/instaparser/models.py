from django.contrib.auth.models import User
from django.db import models


class TaskForParse(models.Model):
    """Модель задач на парсинг."""

    class Status(models.TextChoices):
        WAITING = 'waiting', 'Ожидает'
        IN_PROGRESS = 'in_progress', 'В процессе'
        DONE = 'done', 'Выполнен'

    user = models.ForeignKey(User, related_name='task_for_parse', verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    user_to_scrape = models.CharField(max_length=255, verbose_name='Аккаунт для парсинга')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.WAITING,
                              verbose_name='Статус')
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)

    def __str__(self):
        return f'{self.user}: {self.user_to_scrape}'

    class Meta:
        verbose_name = 'Задача на парсинг'
        verbose_name_plural = 'Задачи на парсинг'


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

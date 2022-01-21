# Generated by Django 4.0.1 on 2022-01-21 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaparser', '0002_taskforparse_created_at_taskforparse_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskforparse',
            old_name='username_for_parse',
            new_name='user_to_scrape',
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=255, verbose_name='Username')),
                ('full_name', models.CharField(default='', max_length=255, verbose_name='ФИО')),
                ('is_private', models.BooleanField(default=False, verbose_name='Приватный ли аккаунт')),
                ('contact_phone_number', models.CharField(default='', max_length=255, verbose_name='Телефон')),
                ('public_email', models.CharField(default='', max_length=255, verbose_name='Email')),
                ('whatsapp_number', models.CharField(default='', max_length=255, verbose_name='Whatsapp')),
                ('biography', models.CharField(default='', max_length=500, verbose_name='Описание профиля')),
                ('follower_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во подписчиков')),
                ('following_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во подписок')),
                ('following_tag_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во подписок на теги')),
                ('media_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во публикаций')),
                ('usertags_count', models.PositiveIntegerField(default=0, verbose_name='Кол-во тегов пользователя')),
                ('business_contact_method', models.CharField(default='', max_length=255, verbose_name='Способ связи')),
                ('instagram_location_id', models.PositiveIntegerField(default=0, verbose_name='id геолокации')),
                ('task_for_parse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_from_parse', to='instaparser.taskforparse', verbose_name='задача на парсинг')),
            ],
            options={
                'verbose_name': 'Cпаршеные данные',
                'verbose_name_plural': 'Cпаршеные данные',
            },
        ),
    ]
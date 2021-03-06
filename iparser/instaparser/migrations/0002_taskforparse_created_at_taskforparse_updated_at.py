# Generated by Django 4.0.1 on 2022-01-20 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instaparser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskforparse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskforparse',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления'),
        ),
    ]

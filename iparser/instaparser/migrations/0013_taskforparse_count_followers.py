# Generated by Django 4.0.1 on 2022-02-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaparser', '0012_instagramaccount_used_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskforparse',
            name='count_followers',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Количество подписчиков'),
        ),
    ]
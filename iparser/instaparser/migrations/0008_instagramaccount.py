# Generated by Django 4.0.1 on 2022-01-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaparser', '0007_alter_taskforparse_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('enc_password', models.CharField(max_length=255, verbose_name='Хэш пароля')),
            ],
        ),
    ]
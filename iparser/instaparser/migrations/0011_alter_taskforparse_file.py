# Generated by Django 4.0.1 on 2022-01-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaparser', '0010_instagramaccount_is_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskforparse',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/', verbose_name=''),
        ),
    ]

# Generated by Django 3.2.13 on 2022-07-27 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_notice_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='role',
        ),
    ]
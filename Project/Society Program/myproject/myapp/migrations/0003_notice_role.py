# Generated by Django 3.2.13 on 2022-07-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_notice_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='role',
            field=models.CharField(default='exit', max_length=10),
            preserve_default=False,
        ),
    ]
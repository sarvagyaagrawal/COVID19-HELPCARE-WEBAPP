# Generated by Django 3.1.3 on 2021-05-23 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20210523_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oxygen',
            name='user',
        ),
    ]

# Generated by Django 3.1.3 on 2021-05-23 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_oxygen_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oxygen',
            name='user',
        ),
    ]

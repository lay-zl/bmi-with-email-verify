# Generated by Django 3.2.12 on 2023-01-19 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_alter_customuser_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='result',
        ),
    ]
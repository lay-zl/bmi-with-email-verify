# Generated by Django 3.2.12 on 2023-01-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_customuser_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='result',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.2.12 on 2023-01-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20230118_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='auth_token',
            field=models.CharField(default=0, max_length=100),
        ),
    ]

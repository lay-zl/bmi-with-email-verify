# Generated by Django 3.2.12 on 2023-01-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_customuser_auth_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='result',
            field=models.CharField(default=False, max_length=100),
        ),
    ]

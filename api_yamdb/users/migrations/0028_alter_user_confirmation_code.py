# Generated by Django 3.2 on 2023-01-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='3b718b42-06c6-4ba0-82af-d3686a93d316', editable=False, max_length=40),
        ),
    ]

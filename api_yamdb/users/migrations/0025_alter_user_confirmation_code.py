# Generated by Django 3.2 on 2023-01-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='2af8991d-fcc6-4fa4-a58b-55d64a141ccf', editable=False, max_length=40),
        ),
    ]

# Generated by Django 3.2 on 2023-01-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='9ae15611-011a-4d6e-b255-135e4e1f3497', editable=False, max_length=40),
        ),
    ]

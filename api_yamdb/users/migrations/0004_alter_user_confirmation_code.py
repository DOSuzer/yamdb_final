# Generated by Django 3.2 on 2022-12-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='fcea67a7-fd64-4a8d-b40a-f07cb8357a68', editable=False, max_length=40, unique=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_alter_age_value_alter_phonenumber_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.DeleteModel(
            name='Age',
        ),
    ]

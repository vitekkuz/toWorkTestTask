# Generated by Django 4.0.6 on 2022-07-16 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_rename_aria_user_area_alter_user_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sex',
            name='value',
        ),
        migrations.AddField(
            model_name='sex',
            name='sex',
            field=models.CharField(choices=[('М', 'Мужчина'), ('Ж', 'Женщина')], default='М', max_length=1, verbose_name='sex'),
            preserve_default=False,
        ),
    ]

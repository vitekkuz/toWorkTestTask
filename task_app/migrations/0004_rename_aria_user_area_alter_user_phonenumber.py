# Generated by Django 4.0.6 on 2022-07-16 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0003_alter_user_age_delete_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='aria',
            new_name='area',
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='task_app.phonenumber'),
        ),
    ]
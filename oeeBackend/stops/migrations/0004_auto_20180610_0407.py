# Generated by Django 2.0.6 on 2018-06-10 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stops', '0003_auto_20180603_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stop',
            old_name='stop_created_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='stop',
            old_name='stop_update_at',
            new_name='update_at',
        ),
    ]
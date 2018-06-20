# Generated by Django 2.0.6 on 2018-06-20 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_orders_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joborderdata',
            name='job_number_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='joborderdata_job_order', to='job_orders.JobOrder'),
        ),
        migrations.AlterField(
            model_name='joborderdata',
            name='shift_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='joborderdata_shift', to='shifts.Shift'),
        ),
    ]

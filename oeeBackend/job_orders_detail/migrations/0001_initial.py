# Generated by Django 2.0.6 on 2018-06-27 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workstations', '__first__'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_order_id', models.IntegerField(blank=True, editable=False, null=True)),
                ('production_rate', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='joborderdetail_item', to='items.Item')),
                ('workstation', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='joborderdetail_workstation', to='workstations.Workstation')),
            ],
        ),
    ]

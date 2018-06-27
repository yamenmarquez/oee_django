# Generated by Django 2.0.6 on 2018-06-27 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        ('workstations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_rate', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bom_item', to='items.Item')),
                ('workstation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bom_workstation', to='workstations.Workstation')),
            ],
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-10 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workstation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ws_name', models.CharField(max_length=256)),
                ('ws_type', models.CharField(choices=[('FA', 'Fabricación'), ('EN', 'Envasado'), ('ET', 'Etiquetado')], max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('ws_plant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plants.Plant')),
            ],
        ),
    ]
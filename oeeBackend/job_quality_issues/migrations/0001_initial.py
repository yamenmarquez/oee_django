# Generated by Django 2.0.6 on 2018-06-20 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quality_issues', '0001_initial'),
        ('job_orders_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobQualityIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_issue_qty', models.IntegerField()),
                ('reworked', models.NullBooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('job_order_data_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='jobqualityissue_q_issue', to='job_orders_data.JobOrderData')),
                ('q_issue_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='jobqualityissue_q_issue', to='quality_issues.QualityIssue')),
            ],
        ),
    ]
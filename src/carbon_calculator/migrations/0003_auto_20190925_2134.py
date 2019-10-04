# Generated by Django 2.2.3 on 2019-09-25 21:34

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0029_auto_20190910_1437'),
        ('carbon_calculator', '0002_auto_20190830_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCQuestion',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100, null=True)),
                ('question_text', models.CharField(max_length=100, null=True)),
                ('question_type', models.CharField(choices=[('C', 'Choice'), ('T', 'Text'), ('N', 'Number')], default='C', max_length=15)),
                ('response_1', models.CharField(max_length=100, null=True)),
                ('skip_1', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('response_2', models.CharField(max_length=100, null=True)),
                ('skip_2', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('response_3', models.CharField(max_length=100, null=True)),
                ('skip_3', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('response_4', models.CharField(max_length=100, null=True)),
                ('skip_4', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('response_5', models.CharField(max_length=100, null=True)),
                ('skip_5', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('response_6', models.CharField(max_length=100, null=True)),
                ('skip_6', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CCStation',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('actions', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ccaction',
            name='id',
        ),
        migrations.AlterField(
            model_name='ccaction',
            name='average_points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ccaction',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='CCEvent',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('shortname', models.CharField(max_length=15, null=True)),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(blank=True, max_length=100)),
                ('host_org', models.CharField(blank=True, max_length=100)),
                ('host_contact', models.CharField(blank=True, max_length=100)),
                ('host_email', models.EmailField(max_length=254)),
                ('host_phone', models.CharField(blank=True, max_length=15)),
                ('host_url', models.URLField(blank=True)),
                ('sponsor_org', models.CharField(blank=True, max_length=100)),
                ('sponsor_url', models.URLField(blank=True)),
                ('host_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_host_logo', to='database.Media')),
                ('sponsor_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_sponsor_logo', to='database.Media')),
                ('stations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ccaction_picture', to='carbon_calculator.CCStation')),
            ],
        ),
    ]
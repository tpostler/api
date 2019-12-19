# Generated by Django 2.2.5 on 2019-11-21 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0066_data_reported_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activity', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.Community')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.UserProfile')),
            ],
            options={
                'db_table': 'activity_logs',
                'ordering': ('activity',),
            },
        ),
    ]
# Generated by Django 2.2.3 on 2019-09-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0028_auto_20190910_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagcollection',
            name='allow_multiple',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

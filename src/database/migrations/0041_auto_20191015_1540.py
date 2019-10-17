# Generated by Django 2.2.5 on 2019-10-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0040_auto_20191010_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='actionproperty',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='billingstatement',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='community',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='emailcategory',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='graph',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='pagesection',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='permission',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='policy',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='slider',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='tagcollection',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='is_published',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
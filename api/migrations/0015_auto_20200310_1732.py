# Generated by Django 2.2.11 on 2020-03-10 17:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200310_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='urls',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, null=True, size=None),
        ),
    ]

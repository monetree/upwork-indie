# Generated by Django 2.2.11 on 2020-03-10 17:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200309_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistprofile',
            name='social_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, size=None),
        ),
    ]

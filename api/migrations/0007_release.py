# Generated by Django 2.2.11 on 2020-03-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_user_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('urls', models.CharField(blank=True, max_length=256, null=True)),
                ('slug', models.CharField(blank=True, max_length=256, null=True)),
                ('photo', models.FileField(blank=True, default=None, null=True, upload_to='')),
            ],
        ),
    ]

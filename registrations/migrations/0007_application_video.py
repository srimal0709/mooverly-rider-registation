# Generated by Django 5.1.4 on 2024-12-23 14:49

import registrations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_alter_application_working_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=registrations.models.Application.upload_to_video),
        ),
    ]

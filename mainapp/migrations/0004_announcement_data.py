# Generated by Django 5.0 on 2023-12-31 11:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_announcement_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

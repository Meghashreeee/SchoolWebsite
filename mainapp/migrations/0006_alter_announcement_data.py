# Generated by Django 5.0 on 2023-12-31 11:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_announcement_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

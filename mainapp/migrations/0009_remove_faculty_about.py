# Generated by Django 5.0 on 2023-12-31 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_faculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='about',
        ),
    ]

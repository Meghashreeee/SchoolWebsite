# Generated by Django 5.0 on 2023-12-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_remove_faculty_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='subjects',
        ),
        migrations.AddField(
            model_name='faculty',
            name='position',
            field=models.CharField(default='Teacher', max_length=100),
        ),
    ]

# Generated by Django 5.0 on 2023-12-31 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_remove_faculty_subjects_faculty_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='faculty'),
        ),
    ]

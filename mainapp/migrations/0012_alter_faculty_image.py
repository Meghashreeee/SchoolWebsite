# Generated by Django 5.0 on 2023-12-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_faculty_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='faculty'),
        ),
    ]
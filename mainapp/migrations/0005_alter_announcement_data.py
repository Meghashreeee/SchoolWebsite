# Generated by Django 5.0 on 2023-12-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_announcement_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]

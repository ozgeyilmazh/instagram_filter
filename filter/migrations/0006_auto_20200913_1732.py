# Generated by Django 2.2.4 on 2020-09-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0005_auto_20200913_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='editted_images',
            field=models.ImageField(blank=True, null=True, upload_to='filters'),
        ),
    ]

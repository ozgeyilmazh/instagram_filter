# Generated by Django 2.2.4 on 2020-09-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0003_images_editted_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='editted_images',
            field=models.ImageField(blank=True, null=True, upload_to='filters'),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0002_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to='uploads/ads'),
        ),
    ]

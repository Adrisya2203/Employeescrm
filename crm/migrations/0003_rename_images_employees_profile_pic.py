# Generated by Django 3.2.18 on 2023-11-09 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_employees_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='images',
            new_name='profile_pic',
        ),
    ]

# Generated by Django 3.2.18 on 2023-11-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='images',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]

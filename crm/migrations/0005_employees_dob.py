# Generated by Django 3.2.18 on 2023-11-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_alter_employees_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]

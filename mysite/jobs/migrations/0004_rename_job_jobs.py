# Generated by Django 4.2.2 on 2023-06-29 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_job_logo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='Jobs',
        ),
    ]
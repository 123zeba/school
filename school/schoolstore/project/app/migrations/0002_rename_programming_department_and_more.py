# Generated by Django 4.1.6 on 2023-02-08 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Programming',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='programming',
            new_name='department',
        ),
    ]

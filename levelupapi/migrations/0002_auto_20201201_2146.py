# Generated by Django 3.1.2 on 2020-12-01 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='day',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='description',
        ),
    ]
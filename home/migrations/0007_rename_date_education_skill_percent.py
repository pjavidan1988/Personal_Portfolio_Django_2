# Generated by Django 3.2.6 on 2021-08-05 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_skill_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='date_education',
            new_name='percent',
        ),
    ]

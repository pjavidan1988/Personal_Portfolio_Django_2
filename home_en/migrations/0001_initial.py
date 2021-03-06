# Generated by Django 3.2.6 on 2021-08-05 02:38

import ckeditor_uploader.fields
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting_en',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('birth_day', models.CharField(max_length=150)),
                ('birth_month', models.CharField(max_length=150)),
                ('birth_year', models.CharField(max_length=150)),
                ('icon', models.ImageField(blank=True, upload_to='images/Icons/%Y/%m/%d/')),
                ('logo', models.ImageField(blank=True, upload_to='images/Logo/%Y/%m/%d/')),
                ('profile_image', models.ImageField(blank=True, upload_to='images/Logo/%Y/%m/%d/')),
                ('facebook', models.CharField(blank=True, max_length=150)),
                ('github', models.CharField(blank=True, max_length=150)),
                ('linkedin', models.CharField(blank=True, max_length=150)),
                ('twitter', models.CharField(blank=True, max_length=150)),
                ('youtube', models.CharField(blank=True, max_length=150)),
                ('whatsapp', models.CharField(blank=True, max_length=150)),
                ('telegram', models.CharField(blank=True, max_length=150)),
                ('instagram', models.CharField(blank=True, max_length=150)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('footer_text', models.CharField(max_length=150)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('references', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('update_at', django_jalali.db.models.jDateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Setting_en',
                'verbose_name_plural': 'Setting_en',
            },
        ),
    ]

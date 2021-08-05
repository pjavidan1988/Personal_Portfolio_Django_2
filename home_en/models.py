from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.

class Setting_en(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=250)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    birth_day = models.CharField(max_length=150)
    birth_month = models.CharField(max_length=150)
    birth_year = models.CharField(max_length=150)
    icon = models.ImageField(blank=True, upload_to='images/Icons/%Y/%m/%d/')
    logo = models.ImageField(blank=True, upload_to='images/Logo/%Y/%m/%d/')
    profile_image = models.ImageField(blank=True, upload_to='images/Logo/%Y/%m/%d/')
    facebook = models.CharField(blank=True, max_length=150)
    github = models.CharField(blank=True, max_length=150)
    linkedin = models.CharField(blank=True, max_length=150)
    instagram = models.CharField(blank=True, max_length=150)
    twitter = models.CharField(blank=True, max_length=150)
    youtube = models.CharField(blank=True, max_length=150)
    whatsapp = models.CharField(blank=True, max_length=150)
    telegram = models.CharField(blank=True, max_length=150)
    instagram = models.CharField(blank=True, max_length=150)
    about = RichTextUploadingField(blank=True)
    footer_text = models.CharField(max_length=150)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = jmodels.jDateField(auto_now_add=True)
    update_at = jmodels.jDateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Setting_en'
        verbose_name_plural = 'Setting_en'

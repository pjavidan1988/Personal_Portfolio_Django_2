from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.

class Setting(models.Model):
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


class Resume(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    university = models.CharField(max_length=150)
    date_education = models.CharField(max_length=150)
    description_education = models.CharField(max_length=255)
    experiences = models.CharField(max_length=150)
    date_experiences = models.CharField(max_length=150)
    description_experiences = models.CharField(max_length=255)
    language_name = models.CharField(max_length=150)
    percent = models.CharField(max_length=150)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = jmodels.jDateField(auto_now_add=True)
    update_at = jmodels.jDateField(auto_now=True)

    def __str__(self):
        return self.university

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resume'


class Skill(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    programming_language = models.CharField(max_length=50, blank=True)
    percent = models.CharField(max_length=50, blank=True)
    status = status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.programming_language


class otherSkill(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50, blank=True)
    percent = models.CharField(max_length=50, blank=True)
    status = status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.skill_name


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    university = models.CharField(max_length=50, blank=True)
    date_education = models.CharField(max_length=150)
    description_education = models.CharField(max_length=255)

    def __str__(self):
        return self.university


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    experiences = models.CharField(max_length=50, blank=True)
    date_experiences = models.CharField(max_length=150)
    description_experiences = models.CharField(max_length=255)

    def __str__(self):
        return self.experiences



class Blog(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(blank=True, upload_to='images/blog/%Y/%m/%d/')
    description = RichTextUploadingField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Skill(models.Model):
    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    class Meta:
        verbose_name = ("UserProfile")
        verbose_name_plural = ("UserProfiles")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar')
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Media(models.Model):
    class Meta:
        verbose_name = ("Media")
        verbose_name_plural = ("Media Files")

    image = models.ImageField(blank=True, null=True, upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Education(models.Model):
    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")

    educational_institution = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(blank=True, null=True, upload_to="education")
    qualification = models.CharField(max_length=25, blank=True, null=True)
    career = models.CharField(max_length=25, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.educational_institution

class WorkExperience(models.Model):
    class Meta:
        verbose_name = ("WorkExperience")
        verbose_name_plural = ("WorkExperiences")

    post = models.CharField(max_length=50, blank=False, null=False)
    job_type = models.CharField(max_length=50, blank=False, null=False)
    company = models.CharField(max_length=50, blank=False, null=False)
    location = models.CharField(max_length=40, blank=False, null=False)
    start_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.post} at {self.company}"

class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = "Certificate"
    
    name = models.CharField(max_length=50,  blank=True, null=True)
    company = models.CharField(max_length=30,  blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    url_credential = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="certificate")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name











































from django.contrib import admin
from . models import (
    Skill,
    UserProfile,
    Media,
    Education,
    WorkExperience,
    Certificate,
)

# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id','educational_institution','qualification')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('id','post','company','location')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name','company')

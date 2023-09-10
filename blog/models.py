from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class Blog(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]
        
    timestamp = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField( blank=True, null=True)
    slug = models.SlugField( blank=True, null=True)
    image=models.ImageField( blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super (Blog, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/blog/{self.slug}"

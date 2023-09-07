from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Portfolio(models.Model):
    class Meta:
        verbose_name = ("Portfolio")
        verbose_name_plural = ("Portfolio Profiles")
        ordering = ['name']

    name = models.CharField(max_length=200, blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"



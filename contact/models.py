from django.db import models

# Create your models here.
class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
        
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    
    def __str__(self):
        return f'{self.name}'

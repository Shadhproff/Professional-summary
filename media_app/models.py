
# Create your models here.
from django.db import models

class MultimediaItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image_file = models.ImageField(upload_to='images/', blank=True, null=True)
    media_file = models.FileField(upload_to='media/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.title
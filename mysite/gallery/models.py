from django.db import models

from django.db import models
from django.urls import reverse

class Image(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='gallery/%Y/%m/%d/')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('gallery:image_list')


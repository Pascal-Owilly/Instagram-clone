from django.db import models
from django.forms import ImageField

# Create your models here.

class Logo_image(models.Model):
    logo = models.ImageField(upload_to = 'media/')

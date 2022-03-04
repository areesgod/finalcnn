from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import CharField
# Create your models here.


class Photo(models.Model):
    image = CloudinaryField('image')
    classification = models.CharField(max_length=300, blank=True)

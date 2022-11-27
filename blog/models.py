from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('D' , 'Draft'),
        ('P' , 'Publish')
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="image")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

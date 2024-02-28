from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    text = models.CharField(max_length=1000000)


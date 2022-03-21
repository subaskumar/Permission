from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    
    def __str__(self):
        return str(self.title)
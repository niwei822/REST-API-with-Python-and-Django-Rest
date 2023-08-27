from django.db import models

# Create your models here.

class Movie(models.Model):
    
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField()

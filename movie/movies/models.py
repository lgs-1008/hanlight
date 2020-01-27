from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=30, primary_key = True, unique = True) #제목
    genre = models.CharField(max_length=15, null = True) #장르
    year = models.IntegerField(null = True)

    def __str__(self):
        return self.title

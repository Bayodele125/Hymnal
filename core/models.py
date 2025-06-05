from django.db import models

# Create your models here.

class Hymn(models.Model):
    title = models.CharField(max_length=200)
    lyrics = models.TextField()
    author = models.CharField(max_length=200, blank=True, null=True)
    sound = models.FileField(upload_to='media', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
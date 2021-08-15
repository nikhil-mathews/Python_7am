from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    desc=models.TextField()

    def __str__(self):
        return f"{self.author} -- {self.title}"

    def get_absolute_url(self):
        return reverse('home')
from django.db import models

# Create your models here.

class CmdRemember(models.Model):
    command=models.CharField(max_length=200)

    def __str__(self):
        return self.command
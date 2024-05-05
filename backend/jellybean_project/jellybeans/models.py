from django.db import models

class Flavor(models.Model):
    Flavor = models.CharField(max_length=100)
    Color = models.CharField(max_length=50)
    Description = models.TextField()

    def __str__(self):
        return self.name



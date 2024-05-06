from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Flavor(models.Model):
    Flavor = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Description = models.TextField()
    Rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name


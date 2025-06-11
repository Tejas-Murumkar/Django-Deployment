from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=100, verbose_name="Film")
    release_year = models.IntegerField(
        max_length=4, 
        verbose_name="Release Year",
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)]
    )
    collection = models.IntegerField(validators=[MinValueValidator(0)])
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    
from django.db import models

# Create your models here.


class Car(models.Model):
    
    CHOICES = [
        ('G', 'GASOLINE'),
        ('D', 'DIESEL')
    ]

    name = models.CharField(max_length=256)
    power = models.IntegerField()
    engine = models.CharField(choices=CHOICES, max_length=64)

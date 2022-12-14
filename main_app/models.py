from operator import mod
from random import choices
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Stuff(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.color} {self.name}'

    def get_absolute_url(self):
        return reverse('stuffs_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stuffs = models.ManyToManyField(Stuff)

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id })

class Feeding(models.Model):
    MEALS = (
    ('B', 'Breakfast'),
    ('D', 'Dinner'),
)
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__ (self):
        return f'{self.get_meal_display()} on {self.date}'

    class Meta: 
        ordering = ['-date']


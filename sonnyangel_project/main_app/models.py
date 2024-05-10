from django.db import models
from django.urls import reverse

# Create your models here.

class Accessories(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})

class Sonnyangel(models.Model):
    series = models.CharField(max_length=100)
    sonnyangelname = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images')

    accessories = models.ManyToManyField(Accessories)

    def __str__(self):
        return self.sonnyangelname

    def get_absolute_url(self):
        return reverse('detail', kwargs={'sonnyangel_id': self.id})

class Feeding(models.Model):
    food = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    sonnyangel = models.ForeignKey(Sonnyangel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.food}{self.description}'
    
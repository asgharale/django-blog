from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cat-detail', kwargs={'address': self.address})


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_deferred_fields(self):
        return reverse('tag-detail', kwargs={"address": self.address})

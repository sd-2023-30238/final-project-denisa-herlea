from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class AnimalManager(models.Manager):
    def get_queryset(self):
        return super(AnimalManager, self).get_queryset().filter(available=True)


class Animal(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pet_creator')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='pets/')
    slug = models.SlugField(max_length=255)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = AnimalManager()

    class Meta:
        verbose_name_plural = 'Animals'
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('adoption:animal_detail', args=[self.slug])


class Adoption(models.Model):

    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    adresa = models.CharField(max_length=250)
    oras = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)



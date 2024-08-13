from django.db import models
from django.urls import reverse_lazy

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Published at')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Image')

    def get_absolute_url(self):
        return reverse_lazy('ViewNews', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name= 'News from Nasa'
        verbose_name_plural = 'Articles'
        ordering = ['-date']



class Astro(models.Model):
    astronaut = models.CharField(max_length=100, verbose_name='Name')
    bio = models.TextField(verbose_name='Bio')
    photo = models.ImageField(verbose_name='Photo')

    def get_absolute_url(self):
        return reverse_lazy('ViewBio', kwargs={'astro_id': self.pk})

    class Meta:
        verbose_name= 'new astronaut'
        verbose_name_plural = 'Astronauts'


class Vehicle(models.Model):
    spaceship = models.CharField(max_length=100, verbose_name='Vehicle')
    about = models.TextField(verbose_name='About')
    photo = models.ImageField(verbose_name='Photo')

    def get_absolute_url(self):
        return reverse_lazy('ViewVehicle', kwargs={'vehicle_id': self.pk})

    class Meta:
        verbose_name= 'new vehicle'
        verbose_name_plural = 'Vehicles'


class LifeInSpace(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    photos = models.ImageField(verbose_name='Image')

    def get_absolute_url(self):
        return reverse_lazy('ViewLive', kwargs={'article_id': self.pk})

    class Meta:
        verbose_name= 'new fact'
        verbose_name_plural = 'Life in Space'



class UniverseList(models.Model):
    space_object = models.CharField(max_length=150, verbose_name='Object')
    read = models.TextField(verbose_name='About')
    photo = models.ImageField(verbose_name='Photo')

    class Meta:
        verbose_name = 'new planet'
        verbose_name_plural = 'SpaceObjects'



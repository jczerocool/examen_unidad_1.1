from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Libro(models.Model):
    name = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    editorial = models.CharField(max_length=120)
    ISBN = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=9999, decimal_places=2)
    slug = models.SlugField(blank=True)  #unique=True

    def __unicode__(self):
        return self.name

def producto_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(producto_pre_save_reciever, sender=Libro)

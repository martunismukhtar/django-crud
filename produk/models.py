from django.db import models
from django.urls import reverse

# Create your models here.

class Produk (models.Model):
    nama = models.CharField(max_length=220)
    
    class Meta:
        db_table = 'produk'

    # def get_absolute_url(self):
    #     return reverse('edit', kwargs={'id': self.id})
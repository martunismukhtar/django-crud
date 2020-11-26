from django.db import models

# Create your models here.

class Penerbit (models.Model):
    nama = models.CharField(max_length=220)
    alamat = models.TextField()

    class Meta:
        db_table = 'penerbit'

class Book(models.Model):
    judul = models.CharField(max_length=220)
    penerbit = models.ForeignKey(Penerbit, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'book'
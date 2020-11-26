# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class TutupanLahan(models.Model):
    nama = models.CharField(max_length=225)
    luas = models.FloatField()
    geom = models.MultiPolygonField()

    def __str__(self):
        return "{}".format(self.nama)

    class Meta:
        db_table="tutupan_lahan"

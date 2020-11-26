# from django.db import models

from django.contrib.gis.db import models

#https://www.webforefront.com/django/modeldatatypesandvalidation.html
#https://docs.djangoproject.com/en/3.1/ref/contrib/gis/model-api/
# Create your models here.
class Media(models.Model):
    username = models.CharField(max_length=225)
    deskripsi = models.TextField()
    # waktu_posting = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.username)

    class Meta:
        db_table="tb_media"

# class TutupanLahan(models.Model):
#     nama = models.CharField(max_length=225)
#     luas = models.FloatField()

#     def __str__(self):
#         return "{}".format(self.nama)

#     class Meta:
#         db_table="tutupan_lahan"
    
# class Zipcode(models.Model):
#     code = models.CharField(max_length=5)
#     poly = models.MultiPolygonField()

#     class Meta:
#         db_table="zip_code"
# Generated by Django 3.1.2 on 2020-10-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelanggan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelanggan',
            name='nama_alat',
        ),
        migrations.RemoveField(
            model_name='pelanggan',
            name='nama_time',
        ),
        migrations.AlterField(
            model_name='pelanggan',
            name='ido_gardu',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='pelanggan',
            name='ido_lama',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='pelanggan',
            name='jenis_app',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pelanggan',
            name='kode_rayon',
            field=models.CharField(max_length=5),
        ),
    ]

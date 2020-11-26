# Generated by Django 3.1.2 on 2020-10-26 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penerbit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=220)),
                ('alamat', models.TextField()),
            ],
            options={
                'db_table': 'penerbit',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=220)),
                ('penerbit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.penerbit')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
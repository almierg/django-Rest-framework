# Generated by Django 4.2.6 on 2023-10-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=150)),
                ('baslik', models.CharField(max_length=150)),
                ('aciklama', models.CharField(max_length=150)),
                ('metin', models.TextField()),
                ('sehir', models.CharField(max_length=150)),
                ('yayınlanma_tarihi', models.DateField()),
                ('aktif', models.BooleanField(default=True)),
                ('yaratılnma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('güncellenme_tarihi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

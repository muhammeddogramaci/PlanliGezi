# Generated by Django 2.2.7 on 2019-12-05 22:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0002_auto_20191205_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='seyahat',
            name='seyahat_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf Ekleyin'),
        ),
        migrations.AlterField(
            model_name='seyahat',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
    ]

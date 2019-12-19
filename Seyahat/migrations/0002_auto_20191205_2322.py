# Generated by Django 2.2.7 on 2019-12-05 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seyahat',
            name='content',
            field=models.TextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='seyahat',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='seyahat',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='seyahat',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
    ]
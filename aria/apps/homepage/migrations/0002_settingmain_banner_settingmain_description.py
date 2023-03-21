# Generated by Django 4.1.7 on 2023-03-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingmain',
            name='banner',
            field=models.ImageField(default=1, upload_to='banners/', verbose_name='Баннер'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settingmain',
            name='description',
            field=models.TextField(default=1, max_length=300, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]

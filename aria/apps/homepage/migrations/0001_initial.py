# Generated by Django 4.1.7 on 2023-03-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название сайта')),
                ('icon', models.ImageField(upload_to='icon/', verbose_name='Иконка')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Лого')),
                ('facebook', models.CharField(max_length=100, verbose_name='Ссылка на Фейсбук')),
                ('twitter', models.CharField(max_length=100, verbose_name='Ссылка на Твиттер')),
                ('description_site', models.TextField(max_length=300, verbose_name='Несколько слов о Сайте')),
                ('activate', models.BooleanField(default=False, verbose_name='Активность настроек')),
            ],
            options={
                'verbose_name': 'Основные настройки',
                'verbose_name_plural': 'Основная настройка',
            },
        ),
    ]

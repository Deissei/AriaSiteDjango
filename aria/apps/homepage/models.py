from django.db import models



class SettingMain(models.Model):
    """Модель Главных настроек""" 
    title = models.CharField("Название сайта", max_length=30)
    description = models.TextField("Описание", max_length=300)

    # images
    icon = models.ImageField("Иконка", upload_to='icon/')
    logo = models.ImageField("Лого", upload_to='logo/')
    banner = models.ImageField("Баннер", upload_to='banners/')

    # socials
    facebook = models.CharField("Ссылка на Фейсбук", max_length=100)
    twitter = models.CharField("Ссылка на Твиттер", max_length=100)
    
    # word_of_site
    description_site = models.TextField("Несколько слов о Сайте", max_length=300)

    # activ
    activate = models.BooleanField("Активность настроек", default=False)

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Основные настройки"
        verbose_name_plural = "Основная настройка"
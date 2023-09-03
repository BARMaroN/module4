from django.db import models
from django.contrib import admin

class Advertisement(models.Model):

    # Заголовок
    #
    title = models.CharField("Заголовок", max_length = 128)

    # Описание
    #
    description = models.TextField("Описание")

    # Цена
    #
    price = models.DecimalField("Цена", max_digits = 10, decimal_places = 2)

    # Уместен ли торг
    #
    auction = models.BooleanField("Торг", help_text = "Отметьте, если хотите торговаться")

    # Дата создания
    created_at = models.DateTimeField(auto_now_add = True)

    # Дата изменения 
    updated_at = models.DateTimeField(auto_now = True)

    @admin.display(description = "Дата создания")
    def created_date(self):
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")


    # Изображения

    # Адрес


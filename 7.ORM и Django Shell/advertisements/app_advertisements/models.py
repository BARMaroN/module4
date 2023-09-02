from django.db import models


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

    # Изображения

    # Адрес


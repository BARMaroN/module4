from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()

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

    @admin.display(description = "Дата создания")
    def created_date(self):
        from django.utils import timezone

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.strftime("%H:%M:%S")
            return format_html("<span style = 'color: green; font-weight:bold;'> Сегодня в {} </span>", created_time)
        
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    # Дата изменения 
    updated_at = models.DateTimeField(auto_now = True)
 
    # Изображения
    image = models.ImageField("Изображение", upload_to = "advertisements/")    

    # Автор
    user = models.ForeignKey(User, verbose_name = "Пользователь", on_delete = models.CASCADE)

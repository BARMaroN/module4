from django.shortcuts import render
from .models import Advertisement


# Функция-представления: "В ответ на наше обращение к сайту (запрос) сайт возвращает нам текст: "Успешно""
def index(request):  
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "index.html", context)


def top_sellers(request):  
    return render(request, "top-sellers.html")


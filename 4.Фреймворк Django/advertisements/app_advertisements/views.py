from django.shortcuts import render
from django.http import HttpResponse


# Функция-представления: "В ответ на наше обращение к сайту (запрос) сайт возвращает нам текст: "Успешно""
def index(request):  
    return HttpResponse("Успешно!")
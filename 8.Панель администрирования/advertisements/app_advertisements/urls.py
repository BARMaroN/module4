from django.urls import path
from .views import index, top_sellers 


# Urlpatterns — это список, содержащий все пути маршрутизации URL-адресов для приложения Django. Он обрабатывается в том порядке, в котором описаны URL-адреса, сверху вниз, до тех пор, пока не будет найден соответствующий маршрут для запроса. Каждый элемент списка urlpatterns обычно содержит объект path() или re_path(), который определяет маршрут URL-адреса, а также имя вызываемой view-функции.  
# path() - отвечает за сопоставление путей и функций-представлений
urlpatterns = [
    path("", index, name="main-page"),
    path("top-sellers/", top_sellers, name="top-sellers")
]
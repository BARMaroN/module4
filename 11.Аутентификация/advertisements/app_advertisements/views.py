from django.shortcuts import render, redirect
from django.urls import reverse 
from .models import Advertisement
from .forms import AdvertisementForm


# Функция-представления: "В ответ на наше обращение к сайту (запрос) сайт возвращает нам текст: "Успешно""
def index(request):  
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "app_advertisements/index.html", context)


def top_sellers(request):  
    return render(request, "app_advertisements/top-sellers.html")

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, "app_advertisements/advertisement-post.html", context)
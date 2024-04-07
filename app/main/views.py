from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here
def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, почему этот магазин такой классный, а товар такой качественный',
    }
    return render(request, 'main/about.html', context)

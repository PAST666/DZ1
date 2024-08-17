from django.shortcuts import render
from datetime import datetime

menu = [
    {
        "name":"Главная",
        "alias":"main",
    },
        {
        "name":"Цены",
        "alias":"price",
    },
        {
        "name":"Записаться на прием",
        "alias":"appointment",
    },
        {
        "name":"Лицензия",
        "alias":"license",
    },
            {
        "name":"Галерея",
        "alias":"gallery",
    },
            {
        "name":"Подготовка к УЗИ",
        "alias":"preparation",
    },
                {
        "name":"Отзывы в 2ГИС",
        "alias":"reviews",
    }
]

def main(request):
    context= {
        "menu": menu,
        "page_alias": "main",
        }
    return render (request, 'main.html', context)

def price(request):
    context= {
        "menu": menu,
        "page_alias": "price",
        }
    return render (request, 'cabinet/price.html', context)

def appointment(request):
    all_time = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30"]
    yesterday = datetime.today()
    min_day_value = yesterday.strftime("%Y-%m-%d")
    context= {
        "menu": menu,
        "page_alias": "appointment",
        "min_day_value": min_day_value,
        "all_time": all_time,
        }
    return render (request, 'cabinet/appointment.html', context)

def license(request):
    context= {
        "menu": menu,
        "page_alias": "license",
        }
    return render (request, 'cabinet/license.html', context)

def gallery(request):
    context= {
        "menu": menu,
        "page_alias": "gallery",
        }
    return render (request, 'cabinet/gallery.html', context)

def preparation(request):
    context= {
        "menu": menu,
        "page_alias": "preparation",
        }
    return render (request, 'cabinet/preparation.html', context)

def reviews(request):
    context= {
        "menu": menu,
        "page_alias": "reviews",
        }
    return render (request, 'cabinet/reviews.html', context)

def thanks_page(request):
    context= {
        "page_alias": "thanks_page",
        }
    return render (request, 'cabinet/thanks_page.html', context)
from django.shortcuts import render

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
    context= {
        "menu": menu,
        "page_alias": "appointment",
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
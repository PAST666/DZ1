from django.shortcuts import render, redirect
# from datetime import datetime
# from .models import Order
from .forms import VisitModelForm
from .models import Visit, Master, License, Gallery

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
    masters = Master.objects.all()
    context= {
        "menu": menu,
        "page_alias": "main",
        'masters': masters,
        }
    return render (request, 'main.html', context)

def price(request):
    context= {
        "menu": menu,
        "page_alias": "price",
        }
    return render (request, 'cabinet/price.html', context)

def appointment(request):
    if request.method == 'POST':
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks_page')
    else:
        form = VisitModelForm()

    context= {
        "menu": menu,
        "page_alias": "appointment",
        'form': form,

        }
    return render(request, 'cabinet/appointment.html', context)

    # return render (request, 'cabinet/appointment.html', context)
    # all_time = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30"]
    # yesterday = datetime.today()
    # min_day_value = yesterday.strftime("%Y-%m-%d")
    # if request.GET.get("date") is None:
    #     context= {
    #         "menu": menu,
    #         "page_alias": "appointment",
    #         "min_day_value": min_day_value,
    #         "all_time": all_time,
    #         "step_1": True,
    #         "step": "Шаг 1"
    #         }
    #     return render (request, 'cabinet/appointment.html', context)
    # else:
    #     appointments=Order.objects.filter(order_day=request.GET.get("date")).all()
    #     print(Order.order_day)
    #     for obj in appointments:
    #         all_time.remove(obj.order_time.strftime("%H:%M"))
    #     context= {
    #         "menu": menu,
    #         "page_alias": "appointment",
    #         "min_day_value": min_day_value,
    #         "all_time": all_time,
    #         "step_1": False,
    #         "step_2": True,
    #         "step": "Шаг 2",
    #         "choised_day": request.GET.get("date"),          
    #         }        
    #     return render (request, 'cabinet/appointment.html', context)


def license(request):
    licenses = License.objects.all()
    context= {
        "menu": menu,
        "page_alias": "license",
        "licenses": licenses
        }
    return render (request, 'cabinet/license.html', context)

def gallery(request):
    gallerys = Gallery.objects.all()
    context= {
        "menu": menu,
        "page_alias": "gallery",
        "gallerys": gallerys
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
    # if request.POST:
    #     name=request.POST["name"]
    #     phone=request.POST["phone"]
    #     day=request.POST["date"]
    #     time=request.POST["time"]
    #     element = Order(
    #         order_name=name,
    #         order_phone=phone,
    #         order_day=day,
    #         order_time=time)
    #     element.save()
        context= {
        "page_alias": "thanks_page",
        # "name": name,

        }
        return render (request, 'cabinet/thanks_page.html', context)
    # else:
    #     context= {
    #     "page_alias": "thanks_page",
    #     }
    #     return render (request, 'cabinet/thanks_page.html', context)
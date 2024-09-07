from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from datetime import datetime
# from .models import Order
from .forms import VisitModelForm
from .models import Visit, Master, License, Gallery, Review, Price
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic import View
from django.views.generic import (
    View,
    TemplateView,
    FormView,
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q

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
    prices= Price.objects.all()
    context= {
        "menu": menu,
        "page_alias": "price",
        "prices": prices
        }
    return render (request, 'cabinet/price.html', context)

class AppointmentView(View):
    def get(self, request):
        form = VisitModelForm()
        context= {
            "menu": menu,
            "page_alias": "appointment",
            'form': form,
            }
        return render(request, 'cabinet/appointment.html', context)
    def post(self, request):
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks_page')
        if form.errors:
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
    reviews = Review.objects.all()
    paginator = Paginator(reviews, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context= {
        "menu": menu,
        "page_alias": "reviews",
        "page_obj": page_obj,
        }
    return render (request, 'cabinet/reviews.html', context)

class ThanksView (View):
    def get (self,request):
        context= {
        "page_alias": "thanks_page",
        }
        return render (request, 'cabinet/thanks_page.html', context)

def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})



class VisitCreateView(CreateView):
    template_name = "cabinet/visit_form.html"
    model = Visit
    form_class = VisitModelForm
    success_url = reverse_lazy('thanks_page')

class VisitDetailView(DetailView):
    template_name = "cabinet/visit_detail.html"
    model = Visit
    context_object_name = "visit"
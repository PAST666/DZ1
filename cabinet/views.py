from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cabinet.permissions import IsAdminOrReadOnly
from .forms import VisitModelForm, VisitEditModelForm
from .models import Visit, Master, License, Gallery, Review, Price, Service
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic import View
from django.urls import reverse_lazy
from django.db.models import Q
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from cabinet.serializers import VisitSerializer, VisitSerializer3
from django.forms import model_to_dict

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
    def get (self, request):
        context= {
        "page_alias": "thanks_page",
        }
        return render (request, 'cabinet/thanks_page.html', context)

class Delete_View (View):
    def get (self, request):
        context= {
        "page_alias": "thanks_page",
        }
        return render (request, 'cabinet/delete_page.html', context)

def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})

#-----------------------------api---------------------------------------------
class VisitApiView(viewsets.ModelViewSet):
    # queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    # http_method_names = ['get']
    permission_classes=(IsAdminOrReadOnly, )
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Visit.objects.all()[:3]
        return Visit.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def service(self, request, pk=None):
        visit = Visit.objects.get(pk=pk)
        services = visit.services.all()
        return Response({'services': [service.name for service in services]})

# class VisitAPIList(generics.ListCreateAPIView):
#     queryset = Visit.objects.all()
#     serializer_class = VisitSerializer

# class VisitAPIUpdate(generics.UpdateAPIView):
#     queryset = Visit.objects.all()
#     serializer_class = VisitSerializer

# class VisitAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Visit.objects.all()
#     serializer_class = VisitSerializer        

# class VisitApiView2(APIView):
#     def get (self, request):
#         queryset = Visit.objects.all().values()
#         return Response({'visits':list(queryset)})
#     def post(self, request):
#         # Получаем данные из запроса
#         post_data = request.data
        
#         # Создаем новый объект Visit из полученных данных
#         visit = Visit.objects.create(
#             name=post_data['name'],
#             phone=post_data['phone'],
#             comment=post_data.get('comment', ''),  # Если комментария нет, будет пустая строка
#             master_id=post_data['master'],  # Используем master_id для связи с мастером
#             status=0  # Устанавливаем начальный статус
#         )
        
#         # Добавляем выбранные услуги через ManyToMany поле
#         if 'services' in post_data:
#             visit.services.set(post_data['services'])
        
#         response_data = {
#             'status': 'Запись успешно создана',
#             'visit': {
#                 'id': visit.id,
#                 'name': visit.name,
#                 'phone': visit.phone,
#                 'comment': visit.comment,
#                 'master_id': visit.master_id,
#                 'status': visit.status,
#                 'services': list(visit.services.values('id', 'name'))
#             }
#         }
#         return Response(response_data)

# class VisitApiView3(APIView):
#     def get (self, request):
#         queryset = Visit.objects.all()
#         return Response({'visits':VisitSerializer3(queryset, many=True).data})
#     def post(self, request):
#         post_data = request.data
#         serializer = VisitSerializer3(data=post_data)
#         serializer.is_valid(raise_exception=True)
#         visit_instance = serializer.save()

#         return Response({'visits': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error':'Method PUT not allowed!'})
#         try:
#             instance = Visit.objects.get(pk=pk)
#         except:
#             return Response({'error':'Object does not exists.'})
#         serializer = VisitSerializer3(data = request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'visits': serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error':'Method DELETE not allowed!'})
#         try:
#             instance = Visit.objects.get(pk=pk)
#             instance.delete()
#         except Visit.DoesNotExist:
#             return Response({'error': 'Object does not exist.'}, status=404)
#         return Response({'message': 'Object deleted successfully!'})
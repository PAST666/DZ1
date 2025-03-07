from django.shortcuts import render
from api2.permissions import IsAdminOrReadOnly
from cabinet.models import Visit
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from api2.serializers import VisitSerializer, VisitSerializer3
from django.forms import model_to_dict

class VisitApiView(viewsets.ModelViewSet):
    # queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    # http_method_names = ['get']
    # permission_classes=(IsAdminOrReadOnly, )
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

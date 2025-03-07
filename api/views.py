from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from api.serializers import VisitSerializer
from api.permissions import IsAdminOrReadOnly
from cabinet.models import Visit


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
        return Response(
            {'services': [service.name for service in services]}
        )

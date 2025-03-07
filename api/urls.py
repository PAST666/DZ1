from django.urls import path, include
from rest_framework import routers

from api.viewsets import VisitApiViewSet

router = routers.DefaultRouter()
router.register(r'api/visit', VisitApiViewSet, basename='visit')

urlpatterns = [
    path("", include(router.urls))
]

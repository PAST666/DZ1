from django.urls import include, path
from rest_framework import routers

from api.viewsets import VisitApiViewSet

router = routers.DefaultRouter()
router.register(r"visit", VisitApiViewSet, basename="visit")

urlpatterns = [path("", include(router.urls))]

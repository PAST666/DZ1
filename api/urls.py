from django.urls import path, include
from rest_framework import routers

from api.views import VisitApiView

router = routers.DefaultRouter()
router.register(r'api/visit', VisitApiView, basename='visit')

urlpatterns = [
    path("", include(router.urls))
]

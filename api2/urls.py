from rest_framework import routers
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api2.views import (
    VisitApiView,
    # VisitApiView2, 
    # VisitApiView3, 
    # VisitAPIList,
    # VisitAPIUpdate,
    # VisitAPIDetailView
)
router = routers.DefaultRouter()
router.register(r'visit', VisitApiView, basename='visit')

urlpatterns = [
    path("", include(router.urls)),
    # path('api/visit2/', VisitApiView2.as_view()),
    # path('api/visit3/', VisitApiView3.as_view()),
    # path('api/visit3/<int:pk>/', VisitApiView3.as_view()),
    # path('api/visit4/', VisitAPIList.as_view()),
    # path('api/visitupdate/<int:pk>/', VisitAPIUpdate.as_view()),
    # path('api/visitcrud/<int:pk>/', VisitAPIDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

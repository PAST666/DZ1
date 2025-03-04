from django.contrib import admin
from django.urls import path, include
from cabinet.views import (
    main,
    price,
    AppointmentView, 
    license, 
    gallery, 
    preparation, 
    reviews, 
    ThanksView, 
    Delete_View, 
    get_services_by_master, 
    VisitApiView, 
    # VisitApiView2, 
    # VisitApiView3, 
    # VisitAPIList,
    # VisitAPIUpdate,
    # VisitAPIDetailView
)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/visit', VisitApiView, basename='visit')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path("price/", price, name="price"),
    path("appointment/", AppointmentView.as_view(), name="appointment"),
    path("license/", license, name="license"),
    path("gallery/", gallery, name="gallery"),
    path("preparation/", preparation, name="preparation"),
    path("reviews/", reviews, name="reviews"),
    path("thanks_page/", ThanksView.as_view(), name="thanks_page"),
    path("delete_page/", Delete_View.as_view(), name="delete_page"),
    path("get_services_by_master/<int:master_id>/", get_services_by_master,
    name="get_services_by_master"),
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

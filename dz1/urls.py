from django.contrib import admin
from django.urls import path
from cabinet.views import main, price, AppointmentView, license, gallery, preparation, reviews, ThanksView, DeleteView, get_services_by_master
from django.conf import settings
from django.conf.urls.static import static
from cabinet.views import (
    VisitCreateView,
    VisitDetailView,
    VisitUpdateView,
    VisitDeleteView,
    ) 


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
    path("delete_page/", DeleteView.as_view(), name="delete_page"),
    path("get_services_by_master/<int:master_id>/", get_services_by_master,
    name="get_services_by_master"),
    path("visit_add/", VisitCreateView.as_view(), name="visit_form"),
    path("visit/<int:pk>/view/", VisitDetailView.as_view(), name="visit_view"),
    path("visit/<int:pk>/edit/", VisitUpdateView.as_view(), name="visit_edit"),
    path("visit/<int:pk>/delete/", VisitDeleteView.as_view(), name="visit_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main, name="main"),
    path("", include("api.urls")),
    path('admin/', admin.site.urls),
    path("price/", price, name="price"),
    path(
        "appointment/",
        AppointmentView.as_view(),
        name="appointment"
    ),
    path("license/", license, name="license"),
    path("gallery/", gallery, name="gallery"),
    path("preparation/", preparation, name="preparation"),
    path("reviews/", reviews, name="reviews"),
    path("thanks_page/", ThanksView.as_view(), name="thanks_page"),
    path("delete_page/", Delete_View.as_view(), name="delete_page"),
    path(
        "get_services_by_master/<int:master_id>/",
        get_services_by_master,
        name="get_services_by_master"
    ),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

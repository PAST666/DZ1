from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cabinet.views import (
    AppointmentView,
    ThanksView,
    agreement,
    gallery,
    get_services_by_master,
    license_page,
    main,
    politika_obrabotki_pd,
    preparation,
    price,
    reviews,
)

urlpatterns = [
    path("", main, name="main"),
    path("admin/", admin.site.urls),
    path("agreement/", agreement, name="agreement"),
    path("price/", price, name="price"),
    path("appointment/", AppointmentView.as_view(), name="appointment"),
    path("license/", license_page, name="license"),
    path("gallery/", gallery, name="gallery"),
    path("politika_obrabotki_pd/", politika_obrabotki_pd, name="politika_obrabotki_pd"),
    path("preparation/", preparation, name="preparation"),
    path("reviews/", reviews, name="reviews"),
    path("thanks_page/", ThanksView.as_view(), name="thanks_page"),
    path(
        "get_services_by_master/<int:master_id>/",
        get_services_by_master,
        name="get_services_by_master",
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

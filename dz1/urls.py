from django.contrib import admin
from django.urls import path
from cabinet import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path("price/", views.price, name="price"),
    path("appointment/", views.appointment, name="appointment"),
    path("license/", views.license, name="license"),
    path("gallery/", views.gallery, name="gallery"),
    path("preparation/", views.preparation, name="preparation"),
    path("reviews/", views.reviews, name="reviews"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

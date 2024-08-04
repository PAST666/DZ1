from django.contrib import admin
from django.urls import path
from cabinet import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),

]

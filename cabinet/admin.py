from django.contrib import admin

from cabinet.models import (
    Gallery,
    License,
    Master,
    Price,
    Review,
    Service,
    Visit,
)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = ("name", "phone", "comment")


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone")
    search_fields = ("first_name", "last_name", "phone")
    list_filter = ("services",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )
    search_fields = ("name", "description")


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ("name", "description")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ("name", "description")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = ("name", "description")


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )
    search_fields = ("name", "price")

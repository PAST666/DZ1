from django.contrib import admin
# from .models import Order

# admin.site.register(Order)
# Register your models here.
from .models import Visit, Master, Service, License, Gallery, Review, Price, SiteVisitor

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'comment')


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('services',)  # Фильтрация по услугам


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name', 'description')
    # filter_horizontal = ('masters',)  # Для удобного выбора множества мастеров

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name', 'price')

@admin.register(SiteVisitor)
class SiteVisitorAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'visited_at', 'views')
    readonly_fields = ('session_id', 'visited_at', 'views')

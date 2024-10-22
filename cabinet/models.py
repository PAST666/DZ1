from tabnanny import verbose
from django.db import models
from django.views.generic import ListView
from django.utils import timezone

# class Order(models.Model):
#     order_dt = models.DateTimeField(auto_now=True)
#     order_name = models.CharField(max_length=200, verbose_name="Имя")
#     order_phone = models.CharField(max_length=200, verbose_name="Телефон")
#     order_day = models.DateField()
#     order_time = models.TimeField()
    
#     def __str__(self) -> str:
#         return self.order_name
    
#     class Meta:
#         verbose_name= "Заказ"   
#         verbose_name_plural= "Заказы"
class Visit(models.Model):

    STATUS_CHOICES = [
        (0, 'Не подтверждена'),
        (1, 'Подтверждена'),
        (2, 'Отменена'),
        (3, 'Выполнена'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус')
    master = models.ForeignKey('Master', on_delete=models.CASCADE, verbose_name='Мастер')
    services = models.ManyToManyField('Service', verbose_name='Услуги')

    def __str__(self):
        return f'{self.name} - {self.phone}'
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

# Класс для мастеров
class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Домашний адрес')
    photo = models.ImageField(upload_to='masters/photos/', blank=True, null=True, verbose_name='Фотография')
    services = models.ManyToManyField('Service', related_name='masters', verbose_name='Услуги')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.phone}'
    
    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

# Класс для услуг
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class License(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='license/photos/', blank=True, null=True, verbose_name='Лицензия')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"

class Gallery(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='gallery/photos/', blank=True, null=True, verbose_name='Галерея')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

class Review(models.Model, ListView):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='review/photos/', blank=True, null=True, verbose_name='Отзыв')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Price(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

class SiteVisitor(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    first_visited_at = models.DateTimeField(verbose_name="Время первого посещения", default=timezone.now)
    last_visited_at = models.DateTimeField(verbose_name="Время последнего посещения", default=timezone.now)
    views = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return f"{self.session_id} - Просмотры: {self.views}"
    
    class Meta:
        verbose_name = "Посетитель сайта"
        verbose_name_plural = "Посетители сайта"
        

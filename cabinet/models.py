from django.db import models


class Visit(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    master = models.ForeignKey('Master', on_delete=models.CASCADE, verbose_name='Мастер')
    services = models.ManyToManyField('Service', verbose_name='Услуги')

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.name} - {self.phone}'


class Master(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Домашний адрес')
    photo = models.ImageField(
        upload_to='masters/photos/',
        blank=True,
        null=True,
        verbose_name='Фотография'
    )
    services = models.ManyToManyField(
        'Service',
        related_name='masters',
        verbose_name='Услуги'
    )

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
        ordering = ("first_name", "last_name")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Service(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class License(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='license/photos/', blank=True, null=True, verbose_name='Лицензия')

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='gallery/photos/', blank=True, null=True, verbose_name='Галерея')

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='review/photos/', blank=True, null=True, verbose_name='Отзыв')

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return self.name

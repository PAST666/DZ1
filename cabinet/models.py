from django.db import models

MAX_NAME_LENGTH = 100
MAX_PHONE_LENGTH = 20
MAX_ADRESS_LENGTH = 255
MAX_NAME_LENGTH_SERVICE = 200
MAX_DIGITS_PRICE = 10
DECIMAL_PLACES_PRICE = 2


class Visit(models.Model):
    name = models.CharField('Имя', max_length=MAX_NAME_LENGTH)
    phone = models.CharField('Телефон', max_length=MAX_PHONE_LENGTH)
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    master = models.ForeignKey('Master', on_delete=models.CASCADE)
    services = models.ManyToManyField('Service', verbose_name='Услуги')

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.name} - {self.phone}'


class Master(models.Model):
    first_name = models.CharField('Имя', max_length=MAX_NAME_LENGTH)
    last_name = models.CharField('Фамилия', max_length=MAX_NAME_LENGTH)
    phone = models.CharField('Телефон', max_length=MAX_PHONE_LENGTH)
    address = models.CharField('Домашний адрес', max_length=MAX_ADRESS_LENGTH)
    photo = models.ImageField(
        'Фотография',
        upload_to='masters/photos/',
        blank=True,
        null=True,
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
    name = models.CharField('Название', max_length=MAX_NAME_LENGTH_SERVICE)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=MAX_DIGITS_PRICE, decimal_places=DECIMAL_PLACES_PRICE)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name

class License(models.Model):
    name = models.CharField('Название', max_length=MAX_NAME_LENGTH)
    description = models.TextField('Описание')
    photo = models.ImageField('Лицензия', upload_to='license/photos/', blank=True, null=True)

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField('Название', max_length=MAX_NAME_LENGTH)
    description = models.TextField('Описание')
    photo = models.ImageField('Галерея', upload_to='gallery/photos/', blank=True, null=True, )

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField('Название', max_length=MAX_NAME_LENGTH)
    description = models.TextField('Описание')
    photo = models.ImageField('Отзыв', upload_to='review/photos/', blank=True, null=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField('Название', max_length=MAX_NAME_LENGTH)
    price = models.IntegerField('Цена')

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"

    def __str__(self):
        return self.name

# Generated by Django 5.0.6 on 2025-04-02 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='gallery/photos/', verbose_name='Галерея')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='license/photos/', verbose_name='Лицензия')),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лицензии',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='review/photos/', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('address', models.CharField(max_length=255, verbose_name='Домашний адрес')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='masters/photos/', verbose_name='Фотография')),
                ('services', models.ManyToManyField(related_name='masters', to='cabinet.service', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
                'ordering': ('first_name', 'last_name'),
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.master')),
                ('services', models.ManyToManyField(to='cabinet.service', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ('-created_at',),
            },
        ),
    ]

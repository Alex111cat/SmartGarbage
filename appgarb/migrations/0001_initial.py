# Generated by Django 3.1.5 on 2021-05-01 00:40

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Methods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('me_method', models.CharField(db_index=True, max_length=40, unique=True, verbose_name='Название метода')),
            ],
            options={
                'verbose_name': 'Метод',
                'verbose_name_plural': 'Методы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Streets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_street', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Название улицы')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
                'ordering': ['s_street'],
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_module', models.CharField(db_index=True, max_length=4, verbose_name='Модуль')),
                ('m_house', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('m_building', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Корпус')),
                ('m_entrance', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Подъезд')),
                ('m_height', models.PositiveSmallIntegerField(verbose_name='Высота установки, в см')),
                ('m_start', models.DateField(default=datetime.date(2021, 5, 1), verbose_name='Дата установки')),
                ('m_is_active', models.BooleanField(default=True, verbose_name='Состояние')),
                ('m_slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('m_cont', models.PositiveSmallIntegerField(default=100, verbose_name='Высота контейнера, в см')),
                ('m_pipe', models.PositiveSmallIntegerField(default=150, verbose_name='Высота мусоропровода')),
                ('m_params', models.TextField(default='{}', verbose_name='Параметры метода')),
                ('m_plan', models.DateField(default=datetime.date(2021, 5, 1), verbose_name='Плановая дата вывоза')),
                ('m_method', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='appgarb.methods', verbose_name='Название метода')),
                ('m_street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appgarb.streets', verbose_name='Название улицы')),
            ],
            options={
                'verbose_name': 'Модуль',
                'verbose_name_plural': 'Модули',
                'ordering': ['m_module'],
                'unique_together': {('m_street', 'm_house', 'm_building', 'm_entrance')},
            },
        ),
        migrations.CreateModel(
            name='Fire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_alarm', models.DateTimeField(verbose_name='Дата и время')),
                ('f_temp', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Температура')),
                ('f_smoke', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Задымленность')),
                ('f_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appgarb.modules', verbose_name='Модуль')),
            ],
            options={
                'verbose_name': 'Пожарная тревога',
                'verbose_name_plural': 'Пожарная тревога',
                'ordering': ['f_module', 'f_alarm'],
                'unique_together': {('f_module', 'f_alarm')},
            },
        ),
        migrations.CreateModel(
            name='Containers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_date', models.DateTimeField(default=datetime.datetime(2021, 5, 1, 6, 0), verbose_name='Дата измерения')),
                ('c_curr', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Дистанция до мусора, см')),
                ('c_is_collected', models.BooleanField(default=False, verbose_name='Мусор вывезен')),
                ('c_incr', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Суточный прирост, %')),
                ('c_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appgarb.modules', verbose_name='Модуль')),
            ],
            options={
                'verbose_name': 'Контейнер',
                'verbose_name_plural': 'Контейнеры',
                'ordering': ['c_module', 'c_date', '-c_is_collected'],
                'unique_together': {('c_module', 'c_date', 'c_is_collected')},
            },
        ),
        migrations.CreateModel(
            name='Analitics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.DateTimeField(default=datetime.datetime(2021, 5, 1, 0, 0), verbose_name='Дата вывоза')),
                ('a_period', models.PositiveSmallIntegerField(verbose_name='Период наполнения, в днях')),
                ('a_fullness', models.PositiveSmallIntegerField(blank=True, default=100, null=True, verbose_name='Уровень наполнения, в %')),
                ('a_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appgarb.modules', verbose_name='Модуль')),
            ],
            options={
                'verbose_name': 'Аналитика',
                'verbose_name_plural': 'Аналитика',
                'ordering': ['a_module', 'a_date'],
                'unique_together': {('a_module', 'a_date')},
            },
        ),
    ]
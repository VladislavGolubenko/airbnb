from django.db import models


# дать всем полям verbose_name
class Booking(models.Model):
    date_start = models.DateField(auto_now_add=True, verbose_name='Дата начала',)  # Время в момент создания
    date_end = models.DateField(verbose_name='Дата окончания', )
    id_realty = models.ForeignKey(
        'Realty',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Недвижимость',
        related_name='realty',
    )
    id_user = models.ForeignKey(
        'User',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Пользователь',
        related_name='user',
    )

    date_creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания',)
    # посмотреть DateTimeField и чтобы заполнялось автоматически с текущи временем
    amount_commission = models.IntegerField(verbose_name='Цена с комиссией',)
    amount = models.IntegerField(verbose_name='Цена без комиссии',)

    class Meta:
        verbose_name = 'Букинг'
        verbose_name_plural = 'Букинг'
        ordering = ['-date_creation']


class User(models.Model):
    full_name = models.CharField(max_length=256, verbose_name='ФИО',)
    number = models.CharField(max_length=17, verbose_name='Номер телефона',)
    email = models.EmailField(verbose_name='электронная почта',)
    passport = models.CharField(max_length=15, verbose_name='Паспортные данные',)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Realty(models.Model):
    type = models.CharField(max_length=250, verbose_name='Тип',)  # Choise, список из возможных вариантов
    rooms = models.IntegerField(verbose_name='Кол-во комнат',)
    bedrooms = models.IntegerField(verbose_name='Кол-во спален',)
    id_img = models.ForeignKey(
        'Pictures',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Изображение',
        related_name='pictures',
    )
    rating = models.CharField(verbose_name='Рэйтинг', max_length=250)
    price = models.FloatField(verbose_name='Цена',)
    region = models.CharField(max_length=250, verbose_name='Регион',)
    address = models.CharField(max_length=150, verbose_name='Адрес',)
    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимости'


class Pictures(models.Model):
    exile = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Ссылка на изображение')
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

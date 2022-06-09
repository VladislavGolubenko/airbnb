from .models import *
from django import forms
from django.contrib.admin import widgets


# Принимаемые атрибуты
# required=True/False - обязательное поле или нет
# initial='изначальное значение'
# empty_label='(Nothing)' - изначальное значение выпадающих списков. если NONE то первый элемент
# widget - все что хотим применить к инпуту

class FormFindHotel(forms.Form):
    hotels_graid = (
        ('1 звезд', '1 звезд'),
        ('2 звезд', '2 звезд'),
        ('3 звезд', '3 звезд'),
        ('4 звезд', '4 звезд'),
        ('5 звезд', '5 звезд'),
    )

    peoples_arrey = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    region_query = Realty.objects.distinct('region').values('region')
    region_array = []
    for key in region_query:
        print(key)
        region = key['region']
        region_array.append([region, region])

    graid = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': "selectpicker show-tick form-control",
                'data-live-search': "true",
                'id': "basic",
            }
        ),
        choices=hotels_graid,
        required=True,
    )

    region = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': "selectpicker show-tick form-control",
                'data-live-search': "true",
                'id': "basic",
            }
        ),
        choices=region_array,
        required=True,
    )

    from_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Когда',
            }
        ),
    )

    peoples = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': "selectpicker show-tick form-control",
                'data-live-search': "true",
                'id': "basic",
            }
        ),
        choices=peoples_arrey,
        required=True,
    )


class FormAddHotel(forms.Form):
    type = forms.CharField(max_length=250, label='Тип', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    rooms = forms.IntegerField(label='Кол-во комнат', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    bedrooms = forms.IntegerField(label='Кол-во спален', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    exile = forms.ImageField(label="Изображение", widget=forms.FileInput(
        attrs={'class': 'form-control'}
    ))
    rating = forms.FloatField(label="Рэйтинг", widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    price = forms.FloatField(label='Цена', widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ))
    region = forms.CharField(max_length=100, label='Регион', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    address = forms.CharField(max_length=100, label='Адрес', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

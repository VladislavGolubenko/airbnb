from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('realty/', realty, name='realty'),
    path('realty/<int:id_realty_id>/', get_booking, name='booking'),
    path('realty/add_realty/', add_realty, name='add_realty'),
]

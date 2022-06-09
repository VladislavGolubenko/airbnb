from django.contrib import admin

from .models import Booking, User, Realty, Pictures


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start', 'date_end', 'id_realty', 'id_user', 'date_creation', 'amount_commission', 'amount')
    list_display_links = ('id',)  # какие поля будут ссылками
    # search_fields = ('airport_name', 'airport_code')  # по каким полям будет происходить поиск
    # list_editable = ('contact_phone',)  # какие поля можно редактировать сразу в таблице
    # list_filter = ('airport_name',)  # для вывода боковых фильтров вывода


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'number', 'email', 'passport')
    list_display_links = ('id',)


class RealtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'rooms', 'bedrooms', 'id_img', 'rating', 'price', 'region', 'address')
    list_display_links = ('id',)


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'exile')
    list_display_links = ('id',)


admin.site.register(Booking, BookingAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Realty, RealtyAdmin)
admin.site.register(Pictures, PicturesAdmin)

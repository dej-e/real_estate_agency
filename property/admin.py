from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address', 'floor', ]
    readonly_fields = ['created_at', ]
    list_display = ['full_address_name', 'price', 'new_building', 'construction_year', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', ]

    def full_address_name(self, obj):
        return obj.town, obj.town_district, obj.address, obj.floor
    full_address_name.short_description = 'Адрес квартиры'

admin.site.register(Flat, FlatAdmin)

from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address', 'floor', ]
    readonly_fields = ['created_at', ]
    list_display = ['full_address_name', 'price', 'new_building', 'construction_year', 'owners_phonenumber',
                    'owner_phone_pure', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', ]
    raw_id_fields = ['liked_by', ]

    def full_address_name(self, obj):
        return obj.town, obj.town_district, obj.address, obj.floor

    full_address_name.short_description = 'Адрес квартиры'


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user', ]
    list_filter = ['flat', 'user', ]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

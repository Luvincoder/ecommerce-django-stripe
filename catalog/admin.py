from django.contrib import admin
from .models import item, Order, Orderitem


class itemAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title', )}
    list_display = [
        'title',
        'price',
        'discount_price'
    ]

admin.site.register(item, itemAdmin)
admin.site.register(Order)
admin.site.register(Orderitem)



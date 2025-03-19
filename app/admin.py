from django.contrib import admin
from .models import *

class CustomersAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "position","image","description")
    list_display_links = ("id", "full_name", "position", "image", "description")

admin.site.register(Customers, CustomersAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "url", "order")
    list_display_links = ("id", "image", "url", "order")

# admin.site.register(Partner, PartnerAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone","description","product","status")
    list_display_links = ("id", "full_name", "phone","description","product","status")
    list_filter = ("status",)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCharacteristic)
admin.site.register(Category)
admin.site.register(News)



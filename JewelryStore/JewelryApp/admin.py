from django.contrib import admin
from .models import Designer, Jewelry


class JewelryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'price',)


class DesignerAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'phone', 'email')


admin.site.register(Jewelry, JewelryAdmin)
admin.site.register(Designer, DesignerAdmin)

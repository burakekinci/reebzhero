from django.contrib import admin
from . models import Product
from . models import extraProduct


class productAdmin(admin.ModelAdmin):
    list_display = ('id','name','category')
    list_display_links = ('id','name')
    list_filter = ('category',)
    list_per_page = 20

# Register your models here.
admin.site.register(Product, productAdmin)

class extraProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    list_per_page = 20

admin.site.register(extraProduct, extraProductAdmin)
from django.contrib import admin
from . models import Product
from . models import SimilarProduct


class productAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    list_per_page = 20

# Register your models here.
admin.site.register(Product, productAdmin)

class similarProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    list_per_page = 20

# Register your models here.
admin.site.register(SimilarProduct,similarProductAdmin)
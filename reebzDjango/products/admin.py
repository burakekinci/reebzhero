from django.contrib import admin
from . models import Product


class productAdmin(admin.ModelAdmin):
    list_display = ('id','name','category','isPublished')
    list_display_links = ('id','name')
    list_filter = ('category',)
    list_editable = ('isPublished',)
    list_per_page = 20

# Register your models here.
admin.site.register(Product, productAdmin)
from django.contrib import admin
from . models import mainPageProduct


class mainPageProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    list_per_page = 20

# Register your models here.
admin.site.register(mainPageProduct, mainPageProductAdmin)
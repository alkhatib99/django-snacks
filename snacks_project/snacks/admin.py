from django.contrib import admin
from .models import ColdDrink,HotDrink

# Register your models here.


@admin.register(ColdDrink)
class AdminColdDrink(admin.ModelAdmin):
    list_display=['name','size','price']
@admin.register(HotDrink)
class AdminHotDrink(admin.ModelAdmin):
    list_display=['name','size','price']
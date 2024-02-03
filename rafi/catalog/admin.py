from django.contrib import admin

# Register your models here.
from .models import Category, Item, PCStuffSize, PCStuffFrequency, PCStuffBrand, HomeStaffRooms, HomeStaffMaterial, HomeStaffBrand

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(PCStuffSize)
admin.site.register(PCStuffFrequency)
admin.site.register(PCStuffBrand)
admin.site.register(HomeStaffRooms)
admin.site.register(HomeStaffMaterial)
admin.site.register(HomeStaffBrand)
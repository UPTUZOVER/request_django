from django.contrib import admin
from .models import *

class ImagesTabularInline(admin.TabularInline):
    model = Images

class TagTabularInline(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTabularInline, TagTabularInline]

admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Contact_us)


# Register ProductAdmin with Product model
admin.site.register(Product, ProductAdmin)
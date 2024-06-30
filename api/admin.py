from django.contrib import admin
from .models import Product, Rating

# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'stars']
    list_filter = ['product', 'user']
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']

admin.site.register(Product,ProductAdmin )
admin.site.register(Rating, RatingAdmin)

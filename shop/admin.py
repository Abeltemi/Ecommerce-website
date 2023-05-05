from django.contrib import admin
from .models import Products, Order

admin.site.site_header = "E-commerce Site"

admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage Ecommerce"
# Register your models here.

class ProductManager(admin.ModelAdmin):
    
    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')
    
    
    list_display = (
        'title',
        'price',
        'discount',
        'category',
        'Description',
    )
    search_fields = ('category', )
    actions = ('change_category_to_default',)

admin.site.register(Products, ProductManager)
admin.site.register(Order)
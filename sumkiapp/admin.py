from django.contrib import admin
from .models import Product, Quickorder, Order, OrderItem, Review, ProductImage, ProductCategory

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','phone','address','created','comment']
#   list_filter = ['created', 'updated']
    inlines = [OrderItemInline]



admin.site.register(Product)
admin.site.register(Quickorder)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)

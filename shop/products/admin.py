from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage, ProductComment

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory_name']
    fields = ('category', 'subcategory_name', 'subcategory_image','image_tag',)
    readonly_fields = ('image_tag',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['subcategory','name','price', 'sizes','created', 'updated']
    inlines = [ProductImageInline]
    search_fields = ['name']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'is_main']
    list_filter = ['is_main']
    readonly_fields = ('thumbnail',)

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'comment']
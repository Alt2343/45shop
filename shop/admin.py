from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductSpecification

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'display_products_count']
    list_filter = ('parent',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    def display_products_count(self, obj):
        return obj.products.count()
    display_products_count.short_description = 'Кол-во товаров'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'available', 'created')
    # Фильтры справа
    list_filter = ('available', 'category', 'created')
    # Поиск по полям
    search_fields = ('name', 'description')
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('name',)}
    # Редактирование прямо из списка
    list_editable = ('price', 'quantity', 'available')
    # Разбивка на страницы
    list_per_page = 50

@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'value')
    list_filter = ('product',)

# Кастомизация внешнего вида
admin.site.site_header = "Панель управления магазином"
admin.site.site_title = "Магазин"
admin.site.index_title = "Администрирование сайта"
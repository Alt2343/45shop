from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория') 
    name = models.CharField(max_length=200, verbose_name='Название товара', help_text='Полное наименование товара для отображения на сайте')
    slug = models.SlugField(max_length=200, unique=True,  verbose_name='URL-адрес', help_text='Уникальная часть URL (например, "iphone-15-pro")')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание', help_text='Подробное описание характеристик товара')
    short_description = models.CharField(max_length=300, blank=True, verbose_name='Краткое описание',help_text='Краткая аннотация для карточек товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text='Цена в рублях')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе', help_text='Доступное количество товара')
    available = models.BooleanField(default=True, verbose_name='Доступен к заказу', help_text='Отображать ли товар в каталоге')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')
    
    class Meta:
        ordering = ['-created']  # Сортировка по дате создания (новые сначала)
        indexes = [
            models.Index(fields=['id', 'slug']),  # Составной индекс
            models.Index(fields=['name']),  # Индекс для поиска по названию
            models.Index(fields=['-created']),  # Индекс для сортировки
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    # Методы модели
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
    
    def in_stock(self):
        """Проверяет, есть ли товар в наличии"""
        return self.quantity > 0
    
    def has_discount(self):
        """Проверяет, есть ли скидка на товар"""
        return self.old_price is not None and self.old_price > self.price
    
    def discount_percent(self):
        """Рассчитывает процент скидки"""
        if self.has_discount():
            return int((1 - self.price / self.old_price) * 100)
        return 0
    
class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    name = models.CharField(max_length=100)  # Название характеристики
    value = models.CharField(max_length=200)  # Значение
    def __str__(self):
        return f"{self.name}: {self.value}"

from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='URL')
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='URL')
    img = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение') # загрузка в папку с годом/месяцем/днем
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена') # max_digits=10 - максимум 10 цифр decimal_places=2 - 2 знака после запятой
    available = models.BooleanField(default=True, verbose_name='Доступно')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    class Meta:
        ordering = ['name']  #Cортировка по имени категории
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
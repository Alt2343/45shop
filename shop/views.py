from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ProductSpecification
# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.product_set.all()  # Пример: товары категории
    return render(request, 'shop/category_detail.html', {
        'category': category,
        'products': products,
    })
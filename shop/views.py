from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ProductSpecification
# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {'categories': categories})

def products(request, slug):
    products = get_object_or_404(Product, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/products_detail.html', {'products': products})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.category_set.all().prefetch_related('products')
    products = category.products.all()
    return render(request, 'shop/category.html', {
        'category': category,
        'subcategories': subcategories,
        'products': products,
    })

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    #path('post/<slug:post_slug>/', views.show_post, name='post'),
    #path('login/', views.login, name='login'),
    path('products/<slug:product_slug>/', views.products, name='product_detail'),
    path('categories/<slug:slug>/', views.category, name='category'),
    path('categories/', views.index, name='index'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
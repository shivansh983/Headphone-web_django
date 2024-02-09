from django.contrib import admin
from django.urls import path, include
from . import views
from shop import views as shop_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('about/',views.about, name = 'about'),
    path('sign/',views.sign, name = 'sign'),
    path('download-cv/', views.download_cv, name='download_cv'),
    path('products/',shop_views.product_list, name = 'product_list'),
    path('add-to-cart/<int:product_id>/', shop_views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', shop_views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/', shop_views.update_quantity, name='update_quantity'),
    path('cart/',shop_views.view_cart, name = 'view_cart')    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name = "home"),
    path("base/", views.BASE),
    path('products/', views.PRODUCT, name="products"),
    path('search/', views.SEARCH, name='search'),
    path('contact/', views.Contact_Page, name='contact'),
    path('products/<str:id>', views.PRODUCT_DETAIL_PAGE, name="product_detail"),
    path('register/', views.HandleRegister, name='register'),
    path('login/', views.Handlelogin, name='login'),
    path('logout/', views.Handlelogout, name='logout'),
    
    
    
    #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
        views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
        views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
        
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

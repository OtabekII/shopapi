from django.urls import path
from . import views

urlpatterns = [
    path('banner/list/', views.banner_list), 
    path('banner/create/', views.banner_create), 
    path('banner/update/<int:id>/', views.banner_update), 
    path('banner/detail/<int:id>/', views.banner_detail), 
    path('banner/delete/<int:id>/', views.banner_delete), 
    
    path('contact/list/', views.contact_list), 
    path('contact/create/', views.contact_create), 
    path('contact/update/<int:id>/', views.contact_update), 
    path('contact/detail/<int:id>/', views.contact_detail), 
    path('contact/delete/<int:id>/', views.contact_delete),
    
    path('product/list/', views.product_list), 
    path('product/create/', views.product_create), 
    path('product/update/<int:id>/', views.product_update),  
    path('product/detail/<int:id>/', views.product_detail), 
    path('product/delete/<int:id>/', views.product_delete),
    
    path('category/list/', views.category_list), 
    path('category/create/', views.category_create), 
    path('category/update/<int:id>/', views.category_update), 
    path('category/delete/<int:id>/', views.category_delete), 
    path('category/detail/<int:id>/', views.category_detail),
    
    path('api/cart/last-achive-cart/', views.LastAchiveCartView.as_view(), name='last_achive_cart'),
    path('api/addproduct/', views.AddProductView.as_view(), name='add_product'),
    path('api/remove-product/', views.RemoveProductView.as_view(), name='remove_product'),
]

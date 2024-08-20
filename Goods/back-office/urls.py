from django.urls import path, include

urlpatterns = [
    path('product/', include('Goods.back-office.product.urls')),
    path('category/', include('Goods.back-office.category.urls')),
    path('enter/', include('Goods.back-office.enter.urls')),
    path('banners/', include('Goods.back-office.banners.urls')),
    path('infos/', include('Goods.back-office.infos.urls'))
]
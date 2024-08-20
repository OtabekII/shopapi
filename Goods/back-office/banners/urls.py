# urls.py
from django.urls import path
from . import views

app_name = 'banners'

urlpatterns = [
    path('list/', views.banner_list, name='banner_list'),
    path('detail/<int:id>/', views.banner_detail, name='banner_detail'),
    path('create/', views.banner_create, name='banner_create'),
    path('update/<int:id>/', views.banner_update, name='banner_update'),
    path('delete/<int:id>/', views.banner_delete, name='banner_delete'),
]

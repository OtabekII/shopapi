
from django.urls import path
from .import views

urlpatterns = [
    path('list/', views.info_list, name='info-list'),
    path('detail/<int:id>/', views.info_detail, name='info-detail'),
    path('create/', views.info_create, name='info-create'),
    path('update/<int:id>/', views.info_update, name='info-update'),
    path('delete/<int:id>/', views.info_delete, name='info-delete'),
]


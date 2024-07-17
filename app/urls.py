from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.index, name='app-index'),
    path('staff/', views.staff, name='app-staff'),
    path('staff_detail/<int:pk>', views.staff_detail, name='app-staff-detail'),
    path('product/', views.product, name='app-product'),
    path('product_delete/<int:pk>/', views.product_delete, name='app-product-delete'),
    path('product_update/<int:pk>/', views.product_update, name='app-product-update'),
    path('order/', views.order, name='app-order')
]
from django.urls import path

from . import views

urlpatterns = [
    path('purchase-stock/', views.purchase_stock, name='purchase-stock'),
    path('purchase-history/', views.purchase_history, name='purchase-history'),
    path('purchase-history/<sku>/edit', views.edit_purchase, name='edit-purchase'),
    path('purchase-history/<sku>', views.delete_purchase, name='delete-purchase')
]
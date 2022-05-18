
from django.urls import path
from . import views


urlpatterns = [
    # PRODUCTS URL
    path('', views.products, name = 'products'),
    path('<int:product_id>', views.product_description, name='product_description'),
    path('new', views.new_product, name='new_product'),
    path('<int:product_id>/edit', views.product_edit, name='product_edit'),
    path('<int:product_id>/delete', views.product_delete, name='product_delete'),

    # WAREHOUSE URL
    path('<int:product_id>/warehouse/<int:warehouse_id>', views.warehouse_description, name='warehouse_description'),
    path('<int:product_id>/warehouse/new', views.new_warehouse, name='new_warehouse'),
    path('<int:product_id>/warehouse/<int:warehouse_id>/edit', views.edit_warehouse, name='edit_warehouse'),
    path('<int:product_id>/warehouse/<int:warehouse_id>/delete', views.delete_warehouse, name='delete_warehouse'),


]

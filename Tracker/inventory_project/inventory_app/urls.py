from django.urls import path
from . import views

urlpatterns = [
    path('', views.shipments, name = 'shipments' ),
    path('<int:shipment_id>', views.shipment_description, name = 'shipment_description' ),
    path('new', views.new_shipment, name='new_shipment'),
    path('<int:shipment_id>/edit', views.shipment_edit, name='shipment_edit'),
    path('<int:shipment_id>/delete', views.delete_shipment, name='delete_shipment'),

    # PRODUCTS

]

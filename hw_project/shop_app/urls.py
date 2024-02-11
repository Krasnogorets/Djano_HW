from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('order/<int:client_id>/', views.show_orders_by_client, name='client_orders'),
    path('orders/<int:client_id>/', views.show_orders_by_period, name='client_orders_by_period'),
    path('addnewproduct/', views.add_new_product, name='add_new_product'),
    path('viewproduct/', views.view_all_products, name='view_all_products'),
    path('updateproduct/<int:product_id>/', views.update_product, name='update_product'),
]


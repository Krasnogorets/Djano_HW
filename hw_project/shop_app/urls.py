from django.urls import path
from . import views

urlpatterns = [
    path('order/<int:client_id>/', views.show_orders_by_client, name='client_orders'),
    path('orders/<int:client_id>/', views.show_orders_by_period, name='client_orders_by_period'),
]

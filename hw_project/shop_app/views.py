from django.shortcuts import render, get_object_or_404
from .models import Order, Product, Client
from django.utils import timezone
from datetime import timedelta


def show_orders_by_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_id=client_id).order_by('-date_of_creation')
    num = len(orders)
    return render(request, 'shop_app/index.html', {'client': client, 'orders': orders, 'num': num})


def show_orders_by_period(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    start_date = timezone.now() - timedelta(days=7)
    week = Product.objects.filter(order__client_id=client_id, order__date_of_creation__gte=start_date) \
                                  .distinct()
    start_date = timezone.now() - timedelta(days=30)
    month = Product.objects.filter(order__client_id=client_id, order__date_of_creation__gte=start_date) \
        .distinct()
    start_date = timezone.now() - timedelta(days=365)
    year = Product.objects.filter(order__client_id=client_id, order__date_of_creation__gte=start_date) \
        .distinct()
    return render(request, 'shop_app/orders_by_data.html',
                  {'client': client, 'week': week, 'month': month, 'year': year})

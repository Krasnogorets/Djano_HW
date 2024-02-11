from django.shortcuts import render, get_object_or_404
from .models import Order, Product, Client
from django.utils import timezone
from datetime import timedelta
from .forms import AddNewProduct
from django.core.files.storage import FileSystemStorage


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

def add_new_product(request):
    if request.method == 'POST' and request.FILES:
        form = AddNewProduct(request.POST,request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            image = form.cleaned_data['picture']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            Product.objects.create(title=title, description=description, price=price,picture=image)
            message = 'продукт добавлен в бд'
            return render(request, 'shop_app/add_product.html', {'form': form, 'message': message})
    else:
        form = AddNewProduct()
        message = 'Заполните форму'
        return render(request, 'shop_app/add_product.html', {'form': form, 'message': message})


def view_all_products(request):
    products = Product.objects.all()
    return render(request,'shop_app/all_product.html', {'products': products})

def update_product(request,product_id):
    if request.method == 'POST' and request.FILES:
        form = AddNewProduct(request.POST,request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            image = form.cleaned_data['picture']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product.objects.filter(pk=product_id).first()
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.picture = image
            product.save()
            message = 'продукт добавлен в бд'
            return render(request, 'shop_app/update_product.html', {'form': form, 'message': message})
    else:
        product = Product.objects.get(pk=product_id)
        form = AddNewProduct(instance=product)
        message = 'внесите нужные исправления в продукт'
        return render(request, 'shop_app/update_product.html', {'form': form, 'message': message})

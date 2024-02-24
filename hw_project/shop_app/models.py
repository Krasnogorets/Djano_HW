"""
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

*Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе данных.
"""
import datetime

from django.db import models
from django.utils.html import format_html


class Client(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=0)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    qts = models.IntegerField(default=1)
    picture = models.ImageField(null=True, blank=True, upload_to="product_img/")
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.price} '

    def picture_view(self):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/ alt="Изображения нет">'.format(self.picture.url))


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    sum = models.DecimalField(default=0, decimal_places=2, max_digits=9)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.sum} '

    def calculate_sum(self):
        total_sum = 0
        for product in self.products.all():
            total_sum += product.price * product.qts
        if self.sum != total_sum:
            self.sum = total_sum
            self.save(update_fields=['sum'])

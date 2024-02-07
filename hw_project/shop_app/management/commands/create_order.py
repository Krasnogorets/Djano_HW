from django.core.management import BaseCommand
from shop_app.models import Order, Product, Client
from random import choice, randint


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_product = Product.objects.all()
        product_lst = [choice(all_product).pk for _ in range(randint(1, 3))]
        all_clients = Client.objects.all()
        client = choice(all_clients)
        order = Order(client=client)
        order.save()
        order.products.add(*product_lst)
        order.calculate_sum()
        order.save()
        self.stdout.write(f'{order} создан')



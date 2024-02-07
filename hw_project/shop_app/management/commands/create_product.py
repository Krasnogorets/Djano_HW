from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from shop_app.models import Product
from random import choice


class Command(BaseCommand):
    def handle(self, *args, **options):
        price_lst = [100, 2000, 3560, 4999]
        for i in range(0, 5):
            product = Product(title=f'{lorem_ipsum.words(2, True)}_{i}',
                              description=lorem_ipsum.paragraph(),
                              price=choice(price_lst),
                              qts=100)
            product.save()
            self.stdout.write(f'{product.title} создан')

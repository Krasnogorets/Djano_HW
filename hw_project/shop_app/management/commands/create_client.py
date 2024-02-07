from django.core.management import BaseCommand
from django.utils import lorem_ipsum
from shop_app.models import Client


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(0,5):
            client = Client(name=f'клиент_{i}',
                            email=f'client_{i}@mail.ru',
                            phone=f"7903903111{i}",
                            address=lorem_ipsum.words(5))
            client.save()
            self.stdout.write(f'{client.name} создан')


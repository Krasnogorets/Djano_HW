from django.core.management.base import BaseCommand
from shop_app.models import Order


class Command(BaseCommand):
    help = "Delete order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            order.delete()
            self.stdout.write(f'заказ: c id={pk} удален')
        else:
            self.stdout.write(f'заказ c id={pk} не найден')


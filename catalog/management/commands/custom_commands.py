from django.core.management.base import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    help = 'Заполняет базу данных новыми данными и очищает старые данные'

    def handle(self, *args, **options):
        # Очистка старых данных
        Product.objects.all().delete()

        # Заполнение базы данных новыми данными
        Product.objects.create(field1='New Value 1', field2='New Value 2')

        self.stdout.write(self.style.SUCCESS('База данный успешно обновлена'))

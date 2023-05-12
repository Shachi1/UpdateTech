import csv
from django.core.management.base import BaseCommand
from sales.models import SalesModel

class Command(BaseCommand):
    help = 'Load data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('xyz_sales_data.csv', type=str, help='/xyz_sales_data.csv')

    def handle(self, *args, **options):
        csv_file_path = options['xyz_sales_data.csv']

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                SalesModel.objects.create(
                    id = int(row['id']),
                    order_id = row['order_id'],
                    order_date = row['order_date'],
                    customer_id = row['customer_id'],
                    sub_category = row['sub_category'],
                    region = row['region'],
                    sales = row['sales']
                )

        self.stdout.write(self.style.SUCCESS('CSV data loaded successfully.'))

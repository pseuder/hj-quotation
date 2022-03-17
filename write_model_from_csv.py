import os
import django
# -------------------------------------------------------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.dev")
django.setup()
# -------------------------------------------------------------------------
from backend.api.models import User, Product
import csv

with open('./csv/User.csv', newline='', encoding='utf-8') as csvfile:
    my_csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in my_csv_reader:
        User.objects.create(
            id = row[0],
            account = row[1],
            password = row[2]
        )


with open('./csv/Product.csv', newline='', encoding='utf-8') as csvfile:
    my_csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in my_csv_reader:
        Product.objects.create(
            id = row[0],
            brand = row[1],
            category = row[2],
            name = row[3],
            unitPrice = row[4]
        )
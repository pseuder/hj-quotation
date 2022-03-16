import os
import django
# -------------------------------------------------------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.dev")
django.setup()
# -------------------------------------------------------------------------
from backend.api.models import Users, Test, Product
import csv

for module in [Users]:
    module.objects.all().delete()

with open('./csv/Users.csv', newline='', encoding='utf-8') as csvfile:
    my_csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in my_csv_reader:
        Users.objects.create(
            user_id = row[0],
            user = row[1],
            password = row[2],
            email = row[3],
            groups = row[4],
            region = row[5],
            record = row[6],
            description = row[7],
            setting = row[8],

        )


with open('./csv/Product.csv', newline='', encoding='utf-8') as csvfile:
    my_csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in my_csv_reader:
        Product.objects.create(
            id = row[0],
            name = row[1],
            price = row[2],
            amount = row[3],
            hot = row[4],
            time = row[5],
            owner = row[6],
            group = row[7],
            url = row[8]
        )
import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings

from users.abstract import Country


class Command(BaseCommand):
    help = 'create countries to the database table from csv file'

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'fixtures/country.csv'), 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip first line
            for row in reader:
                print(row[0])
                country, created = Country.objects.get_or_create(
                    name_iso_3166_a2=row[0],
                    printable_name=row[1],
                    name=row[2],
                )
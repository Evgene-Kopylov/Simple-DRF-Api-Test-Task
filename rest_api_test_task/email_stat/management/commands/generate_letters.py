from django.core.management.base import BaseCommand, CommandError

from factory.faker import faker
import datetime


class Command(BaseCommand):
    help = 'Generate latters in db'

    def handle(self, *args, **options):
        print('How many?')
        n = int(input())
        for i in range(n):
        # for i in range(5):
            self.generate_latters_history()

    def generate_latters_history(self):
        fake = faker.Faker()
        print(
            fake.email(), 
            fake.date_time_between(datetime.datetime.now(), datetime.timedelta(days=7)),
            fake.name()
            )


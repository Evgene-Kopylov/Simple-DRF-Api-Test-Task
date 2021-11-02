from django.core.management.base import BaseCommand, CommandError

from factory.faker import faker
import datetime

from email_stat.models import Letter
import random

class Command(BaseCommand):
    help = 'Generate latters in db'

    def handle(self, *args, **options):
        print('How many?')
        n = int(input())
        for i in range(n):
            self.generate_latters_history()

    def generate_latters_history(self):
        fake = faker.Faker()
        print(
            
            )
        email = fake.email()
        letter = Letter(
            email = email,
            date = fake.date_time_between(
                datetime.datetime.now(), 
                datetime.timedelta(days=7),
                ),
            theme = fake.name()
        )
        letter.save()
        for i in range(-10, 10): # generate with same address
            if i > 1:
                for j in range(i):
                    letter = Letter(
                        email = email,
                        date = fake.date_time_between(
                            datetime.datetime.now(), 
                            datetime.timedelta(days=7),
                            ),
                        theme = fake.name()
                    )
                    letter.save()


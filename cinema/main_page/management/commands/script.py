from django.core.management.base import BaseCommand
from administrator.models import FilmModel, HallModel, SeanceModel, CinemaModel
import random
from faker import Faker
from django.utils import timezone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='how many sessions generate')

    def handle(self, *args, **options):
        fake = Faker()
        count_film = FilmModel.objects.all()
        count_hall = HallModel.objects.all()
        count_cinema = CinemaModel.objects.all()
        for _ in range(options['number']):
            SeanceModel.objects.create(
                film=random.choice(count_film),
                hall=random.choice(count_hall),
                cinema = random.choice(count_cinema),
                price=random.randrange(50, 200, 5),
                time=fake.date_time_between_dates(datetime_start='now',
                                                      datetime_end='+10days', tzinfo=timezone.timezone.utc),
                is_3d=random.randrange(0, 1),
                is_dbox=random.randrange(0, 1),
                is_vip=random.randrange(0, 1),
            )
            
        print(str(options['number']) + ' sessions successfully create')
        
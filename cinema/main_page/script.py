# time
# film
# hall
# price
# cinema
# data
import os
import random
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] =  "cinema.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinema.settings")
import django
django.setup()

from administrator.models import *
import datetime
from faker import Faker
fake = Faker()
# def script():
#     cinema_model = CinemaModel.objects.all()
#     hall_model = HallModel.objects.all()
#     film_model = FilmModel.objects.all()

#     date_today = datetime.datetime.today()

#     for item in range(1, 10):
#         days = date_today + datetime.timedelta(item)
#         if days.day < 10:
#             day_all = ("0"+str(days.day)+"."+str(days.month))
#         else:
#             day_all = (str(days.day)+"."+str(days.month))
#         cinema = [cinema_item.title for cinema_item in cinema_model]
#         cinemas = " ".join(random.sample(cinema, k=1))
#         hall =  [hall_item.title for hall_item in hall_model]
#         halls = " ".join(random.sample(hall, k=1))
#         film = [film_item.title for film_item in film_model]
#         films = " ".join(random.sample(film, k=1))
        
        
#         time_and_price = [
        #     {"time":"10:00", 
        #         "price": 60,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     {"time":"11:00", 
        #         "price": 65,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     {"time":"12:00",  
        #         "price": 60,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     {"time":"13:00", 
        #         "price": 80,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     {"time":"14:00", 
        #         "price": 70,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     {"time":"15:00", 
        #         "price": 65,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     {"time":"16:00",  
        #         "price": 65,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     { "time":"18:00",  
        #         "price": 70,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     {"time":"19:00", 
        #         "price": 75,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        #     {"time":"20:00",
        #         "price": 80,
        #         "day": day_all,
        #         "cinema": cinemas,
        #         "hall": halls,
        #         "film": films},
        # ]
        
        # for item in time_and_price:
        #     seance = SeanceModel.objects.create(
        #         hall=HallModel.objects.get(title=item.get('hall')),
        #         cinema=CinemaModel.objects.get(title=item.get('cinema')),
        #         film = FilmModel.objects.get(title=item.get('film')),
        #         price=item['price'],
        #         time=item.get('time'),
        #         date = item.get('day')
        #     )
        #     seance.save()
        
    


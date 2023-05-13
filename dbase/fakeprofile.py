import random
from faker import Faker
from datetime import date
from models import Profile, Settings, Images


async def add_fake_profile(tg_id: int,
                      tg_url: str,
                      name: str,
                      bdate: date,
                      sex: int,
                      city: str,
                      geo_lat: float,
                      geo_long: float,
                      description: str):
    profile = Profile(tg_id=tg_id, tg_url=tg_url, name=name, bdate=bdate, sex=sex, city=city,
                      description=description, status='active', geo_lat=geo_lat, geo_long=geo_long)
    await profile.create()
    return profile.id


async def add_fake_profile():
    find_list = [[1], [2], [1, 2]]
    purposes_list = [
        [1],
        [2],
        [3],
        [4],
        [5],
        [1, 3],
        [2, 4],
        [3, 5],
        [2, 3],
        [2, 5],
        [4, 5],
        [3, 4, 5],
        [2, 3, 4],
        [1, 2, 3, 4],
        [1, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ]
    fake = Faker(locale='ru-RU')
    name = fake.first_name()
    age = random.randint(20, 40)
    sex = random.randint(1, 2)
    sex_f = find_list[random.randint(0, 2)]
    bdate = date(year=random.randint(1980, 2005), month=random.randint(1, 12), day=random.randint(1, 28))
    city = 'Санкт-Петербург'
    latitude = format(random.uniform(59.809295, 60.089799), '.6f')
    longitude = format(random.uniform(30.183365, 30.457843), '.6f')
    purposes = purposes_list[random.randint(0, 15)]
    tg_id = random.randint(164168462, 942584362)
    tg_url = f'tg://user?id={tg_id}'
    description = f'ПОЛ: {sex}\n{fake.text()}'
    id = await add_fake_profile(tg_id=tg_id, tg_url=tg_url, name=name, bdate=bdate, sex=sex, city=city, geo_lat=latitude,
                                geo_long=longitude, description=description)


add_fake_profile()
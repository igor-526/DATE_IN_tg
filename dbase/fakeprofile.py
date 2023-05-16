import random
from faker import Faker
from datetime import date
from models import Profile, Settings, Images
from datetime import datetime


async def add_fake_profile_db(tg_id: int,
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


async def add_fake_settings(profile: int,
                            age_min: int,
                            age_max: int,
                            find_m: int,
                            find_f: int,
                            purp1: int,
                            purp2: int,
                            purp3: int,
                            purp4: int,
                            purp5: int,
                       ):
    settings = Settings(profile_id=profile, age_min=age_min, age_max=age_max, find_m=find_m, find_f=find_f, purp1=purp1,
                        purp2=purp2, purp3=purp3, purp4=purp4, purp5=purp5, created=date.today(),
                        last_usage=datetime.now())
    await settings.create()


async def add_fake_profile_photos(profile: int,
                                  photos: list):
    for photo in photos:
        image = Images(profile_id=profile, url=photo['url'], url_vk=photo['vk'],
                       description='profile_photo')
        await image.create()


async def add_fake_profile():
    fake = Faker(locale='ru-RU')
    name = fake.first_name()
    age_min = random.randint(18, 25)
    age_max = random.randint(20, 40)
    sex = random.randint(1, 2)
    bdate = date(year=random.randint(1980, 2005), month=random.randint(1, 12), day=random.randint(1, 28))
    city = 'Санкт-Петербург'
    latitude = format(random.uniform(59.809295, 60.089799), '.6f')
    longitude = format(random.uniform(30.183365, 30.457843), '.6f')
    purp1 = random.randint(0, 1)
    purp2 = random.randint(0, 1)
    purp3 = random.randint(0, 1)
    purp4 = random.randint(0, 1)
    purp5 = random.randint(0, 1)
    find_m = random.randint(0, 1)
    find_f = random.randint(0, 1)
    tg_id = random.randint(164168462, 942584362)
    tg_url = f'tg://user?id={tg_id}'
    description = f'ПОЛ: {sex}\n{fake.text()}'
    photos = [{'url': 'https://sun9-59.userapi.com/impg/nSV2ytW4xzJPdSZFlQEXWJJT9r-nGmAob-WFoA/8JN-mTdCT5c.jpg?size=510x340&quality=96&sign=a0393022050ece2dd173c6bd0181ff24&c_uniq_tag=f2aOOfr9TWMpcL3X3IhO-ywsdhDtNlsE8jY_qB1Unqo&type=album', 'vk': 'photo28964076_457273029_8628e7b48b5a8b222a'},
              {'url': 'https://sun9-40.userapi.com/impg/07L9U2iHnF8YmC_c7f1-vt9bXG7B0nWjpMoicQ/z2xe848JxL4.jpg?size=510x348&quality=96&sign=6d690bc2202e4526cd252cfe36a0e018&c_uniq_tag=34jy6ta9SUZOubIuyKIPfXTln7AFkT5sq9UtlfEdfzk&type=album', 'vk': 'photo28964076_457273030_05197b8ed0dc51bd90'},
              {'url': 'https://sun9-62.userapi.com/impg/OscWBrpiA-Xk5cUkXcQFAfOLEVQLudjnRlWnuA/ysk94D1mqo8.jpg?size=510x340&quality=96&crop=5,0,1249,833&sign=05667b9b861625b33f1019a8c70806ff&c_uniq_tag=upVg1O98jO7Z7Spb1VZgqTYBm56bQfTlNzzVrgcaJFw&type=album', 'vk': 'photo28964076_457273031_45f03a2f6bcbdc9808'},
              {'url': 'https://sun9-15.userapi.com/impg/lFxhOmzi2uZqpdmmW3TR3oCKYEuKtZzPUcgiNg/QpkxGD5ce2E.jpg?size=510x340&quality=96&sign=c423fc01107d342108d4a4c310dbeecf&c_uniq_tag=AOPrXw7O9fiVTBH84nTGhoqEdt1IDcWJzyRSGiAHPTE&type=album', 'vk': 'photo28964076_457273032_8ce33c50c57e505926'},
              {'url': 'https://sun9-53.userapi.com/impg/72rZlFlOo3nC5w_WRFhurGiK3nWb-g6QmG8w8A/l7h0Zv7lYa0.jpg?size=510x340&quality=96&sign=31200e9d43fc700e6e3f14ca614abea8&c_uniq_tag=Yc4Qw-EdeTfFkQKexOZYNaNU8K--zvPjmG2Q7Q-H8Tk&type=album', 'vk': 'photo28964076_457273033_bf4629d313e0befac1'},
              {'url': 'https://sun9-61.userapi.com/impg/6cs3YXbHvK2k6khaOLHC8xtxIvyJUqday-9RKw/HR29NGXENbA.jpg?size=510x340&quality=96&sign=88df7113a4b4645851ff9934119f294f&c_uniq_tag=jJbvM2_RjCcOycYF5s6JbZebqIwPmdLE7qAe3q4_jnU&type=album', 'vk': 'photo28964076_457273034_24a3f6f9e8b9efbbec'},]
    photo_list = []
    if sex == 2:
        for _ in range (0, random.randint(1, 10)):
            photo_list.append(photos[random.randint(0, 2)])
    elif sex == 1:
        for _ in range (0, random.randint(1, 10)):
            photo_list.append(photos[random.randint(3, 5)])
    pid = await add_fake_profile_db(tg_id=tg_id, tg_url=tg_url, name=name, bdate=bdate, sex=sex, city=city,
                                    geo_lat=float(latitude), geo_long=float(longitude), description=description)
    await add_fake_settings(profile=pid, age_min=age_min, age_max=age_max, find_m=find_m, find_f=find_f, purp1=purp1,
                            purp2=purp2, purp3=purp3, purp4=purp4, purp5=purp5)
    await add_fake_profile_photos(profile=pid, photos=photo_list)

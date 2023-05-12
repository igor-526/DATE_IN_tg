from datetime import date, datetime
from models import Profile, Settings, Images
from create_bot import bot


async def uploadphotos(file_id: list):
    ready = []
    for photo in file_id:
        file = await bot.get_file(photo)
        url = bot.get_file_url(file['file_path'])
        ready.append({'tg_id': photo, 'url': url})
    return ready


async def add_profile(tg_id: int,
                      tg_nick: str,
                      tg_url: str,
                      name: str,
                      bdate: date,
                      sex: int,
                      city: str,
                      geo_lat: float,
                      geo_long: float,
                      description: str):
    profile = Profile(tg_id=tg_id, tg_nick=tg_nick, tg_url=tg_url, name=name, bdate=bdate, sex=sex, city=city,
                      description=description, status='active', geo_lat=geo_lat, geo_long=geo_long)
    await profile.create()
    return profile.id


async def add_settings(tg_id: int,
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
    profile = await Profile.query.where(Profile.tg_id == tg_id).gino.first()
    settings = Settings(profile_id=profile.id, age_min=age_min, age_max=age_max, find_m=find_m, find_f=find_f, purp1=purp1,
                        purp2=purp2, purp3=purp3, purp4=purp4, purp5=purp5, created=date.today(),
                        last_usage=datetime.now())
    await settings.create()


async def add_profile_photos(tg_id: int,
                             photos: list):
    profile = await Profile.query.where(Profile.tg_id == tg_id).gino.first()
    ready = await uploadphotos(photos)
    for photo in ready:
        image = Images(profile_id=profile.id, url=photo["url"], tg_id=photo["tg_id"],
                       description='profile_photo')
        await image.create()


async def add_tg_id(prof_id: int,
                    tg_id: int,
                    tg_nick: str,
                    tg_url: str):
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    await profile.update(tg_id=tg_id, tg_nick=tg_nick, tg_url=tg_url, status='active').apply()

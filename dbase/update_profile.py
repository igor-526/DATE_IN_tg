from models import Profile, Settings, Images
from dbase.tgtoid import get_profile_id
from dbase.register_profile import uploadphotos
import datetime


async def upd_name(tg_id, name):
    prof_id = await get_profile_id(tg_id)
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    await profile.update(name=name).apply()
    await settings.update(ch_name=datetime.datetime.now()).apply()


async def upd_bdate(tg_id, bdate):
    prof_id = await get_profile_id(tg_id)
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    await profile.update(bdate=bdate).apply()
    await settings.update(ch_bdate=datetime.datetime.now()).apply()


async def upd_sex(tg_id, sex):
    prof_id = await get_profile_id(tg_id)
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    await profile.update(sex=sex).apply()
    await settings.update(ch_sex=datetime.datetime.now()).apply()


async def upd_purposes(tg_id,
                       purps: list):
    prof_id = await get_profile_id(tg_id)
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    purp1 = 1 if 1 in purps else 0
    purp2 = 1 if 2 in purps else 0
    purp3 = 1 if 3 in purps else 0
    purp4 = 1 if 4 in purps else 0
    purp5 = 1 if 5 in purps else 0
    await settings.update(purp1=purp1, purp2=purp2, purp3=purp3, purp4=purp4, purp5=purp5).apply()


async def upd_geo(tg_id, geo):
    prof_id = await get_profile_id(tg_id)
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    await profile.update(city=geo['city'], geo_lat=geo['latitude'],
                         geo_long=geo['longitude']).apply()


async def upd_description(tg_id, description):
    prof_id = await get_profile_id(tg_id)
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    await profile.update(description=description).apply()


async def upd_c_photos(tg_id):
    prof_id = await get_profile_id(tg_id)
    photos = await Images.query.where(Images.profile_id == prof_id).where(Images.description == 'profile_photo').gino.all()
    return len(photos)


async def upd_add_photos(tg_id: int,
                         photos: list):
    profile = await Profile.query.where(Profile.tg_id == tg_id).gino.first()
    ready = await uploadphotos(photos)
    for photo in ready:
        image = Images(profile_id=profile.id, url=photo["url"], tg_id=photo["tg_id"],
                       description='profile_photo')
        await image.create()


async def upd_del_photos(tg_id):
    prof_id = await get_profile_id(tg_id)
    photos = await Images.query.where(Images.profile_id == prof_id).where(Images.description == 'profile_photo').gino.all()
    for photo in photos:
        await photo.delete()


async def upd_sex_f(vk_id, sex_f: list):
    prof_id = await get_profile_id(vk_id)
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    find_m = 1 if 2 in sex_f else 0
    find_f = 1 if 1 in sex_f else 0
    await settings.update(find_m=find_m, find_f=find_f).apply()


async def upd_age_f(tg_id, age_min, age_max):
    prof_id = await get_profile_id(tg_id)
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    await settings.update(age_min=age_min, age_max=age_max).apply()


async def upd_dist(prof_id, dist):
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    await settings.update(km_limit=dist).apply()


async def upd_deactivate_profile(prof_id):
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    await profile.update(status='deactivated').apply()
    await settings.update(deactivated=datetime.datetime.now()).apply()


async def upd_activate_profile(prof_id):
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    await profile.update(status='active').apply()
    await settings.update(deactivated=None).apply()


async def upd_delete_profile(tg_id):
    prof_id = await get_profile_id(tg_id)
    profile = await Profile.query.where(Profile.id == prof_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    photos = await Images.query.where(Images.profile_id == prof_id).where(
        Images.description == 'profile_photo').gino.all()
    for photo in photos:
        await photo.delete()
    await settings.delete()
    await profile.delete()


async def upd_d_height(pr_id, height=None):
    profile = await Profile.query.where(Profile.id == pr_id).gino.first()
    await profile.update(height=height).apply()


async def upd_d_habits(pr_id, habits=None):
    profile = await Profile.query.where(Profile.id == pr_id).gino.first()
    await profile.update(habits=habits).apply()


async def upd_d_children(pr_id, children=None):
    profile = await Profile.query.where(Profile.id == pr_id).gino.first()
    await profile.update(children=children).apply()


async def upd_d_busy(pr_id, busy=None):
    profile = await Profile.query.where(Profile.id == pr_id).gino.first()
    await profile.update(busy=busy).apply()


async def upd_d_hobby(pr_id, hobby=None):
    profile = await Profile.query.where(Profile.id == pr_id).gino.first()
    await profile.update(hobby=hobby).apply()


async def upd_d_animals(pr_id, animals=None):
    profile = await Profile.query.where(Profile.id == pr_id).gino.first()
    await profile.update(animals=animals).apply()

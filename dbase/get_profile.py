from models import Profile, Settings, Images


async def get_prof_forview(id):
    profile = await Profile.query.where(Profile.id == id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == id).gino.first()
    photos = await Images.query.where(Images.profile_id == id).where(Images.description == 'profile_photo').gino.all()
    counter = 0
    images = []
    main_photo = None
    for photo in photos:
        counter += 1
        if counter == 1:
            main_photo = photo.tg_id if photo.tg_id else photo.url
        else:
            images.append(photo.tg_id if photo.tg_id else photo.url)
    purposes = []
    if settings.purp1 == 1:
        purposes.append(1)
    if settings.purp2 == 1:
        purposes.append(2)
    if settings.purp3 == 1:
        purposes.append(3)
    if settings.purp4 == 1:
        purposes.append(4)
    if settings.purp5 == 1:
        purposes.append(5)
    cont_vk = f'https://vk.com/id{profile.vk_id}' if profile.vk_id else None
    cont_tg = profile.tg_url if profile.tg_url else None
    result = {'id': profile.id, 'name': profile.name, 'city': profile.city, 'bdate': profile.bdate,
              'description': profile.description, 'main_photo': main_photo, 'other_photos': images,
              'purposes': purposes, 'cont_vk': cont_vk, 'cont_tg': cont_tg}
    return result


async def get_prof_forsetting(tg_id):
    profile = await Profile.query.where(Profile.tg_id == tg_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == profile.id).gino.first()
    photos = await Images.query.where(Images.profile_id == profile.id).where(Images.description == 'profile_photo').gino.all()
    counter = 0
    images = []
    main_photo = None
    for photo in photos:
        counter += 1
        if counter == 1:
            main_photo = photo.tg_id if photo.tg_id else photo.url
        else:
            images.append(photo.tg_id if photo.tg_id else photo.url)
    purposes = []
    if settings.purp1 == 1:
        purposes.append(1)
    if settings.purp2 == 1:
        purposes.append(2)
    if settings.purp3 == 1:
        purposes.append(3)
    if settings.purp4 == 1:
        purposes.append(4)
    if settings.purp5 == 1:
        purposes.append(5)
    result = {'id': profile.id, 'name': profile.name, 'city': profile.city, 'bdate': profile.bdate,
              'description': profile.description, 'main_photo': main_photo, 'other_photos': images,
              'purposes': purposes, 'sex': profile.sex, 'age_min': settings.age_min, 'age_max': settings.age_max,
              'find_m': settings.find_m, 'find_f': settings.find_f}
    return result


async def get_photos(pr_id):
    photos = await Images.query.where(Images.profile_id == pr_id).where(
        Images.description == 'profile_photo').gino.all()
    result = []
    for photo in photos:
        result.append(photo.tg_id if photo.tg_id else photo.url)
    return result[1:]
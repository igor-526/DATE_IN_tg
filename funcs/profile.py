from dbase import get_prof_forview, get_prof_forsetting
from funcs.bdate_to_info import get_bdate_info
from funcs.purposes import get_purposes_from_list


async def generate_profile_forview(id, dist=None):
    profile = await get_prof_forview(id)
    bdate_info = await get_bdate_info(profile["bdate"])
    msg1 = f'{profile["name"]}, {bdate_info["age"]} (&#127380;{profile["id"]})\n'
    msg1 += f'{dist} км от тебя\n' if dist else ''
    msg1 += f'{profile["city"]}\n\nЦели:\n'
    purposes = await get_purposes_from_list(profile['purposes'])
    for purpose in purposes:
        msg1 += f'&#10004;{purpose}\n'
    msg2 = profile["description"]
    main_photo = profile['main_photo']
    other_photos = profile['other_photos']
    contacts = {'cont_vk': profile['cont_vk'], 'cont_tg': profile['cont_tg']}
    return {'msg1': msg1, 'msg2': msg2, 'm_ph': main_photo, 'o_ph': other_photos, 'contacts': contacts}


async def generate_profile_forsettings(tg_id):
    profile = await get_prof_forsetting(tg_id)
    if profile["find_f"] == 1 and profile["find_m"] == 1:
        findsex = 'девушек и мужчин'
    elif profile["find_f"] == 1:
        findsex = 'только девушек'
    elif profile["find_m"] == 1:
        findsex = 'только мужчин'
    msg1 = f'&#127380;{profile["id"]}\n' \
           f'Имя: {profile["name"]}\n' \
           f'Дата рождения: {profile["bdate"]}\n' \
           f'Город: {profile["city"]}\n' \
           f'Пол: {"мужской" if profile["sex"] == 2 else "женский"}\n' \
           f'Вы  ищете: {findsex}\n' \
           f'От {profile["age_min"]} до {profile["age_max"]} лет\n' \
           f'Ваши цели:\n'
    purposes = await get_purposes_from_list(profile['purposes'])
    for purpose in purposes:
        msg1 += f'&#10004;{purpose}\n'
    msg2 = f'Описание: {profile["description"]}\n\nХотите что-нибудь поменять?'
    att1 = profile['main_photo']
    att2 = profile['other_photos']
    return {'msg1': msg1, 'msg2': msg2, 'att1': att1, 'att2': att2}


async def get_id_from_message(message):
    message = message.split('(')[1]
    message = message.split(')')[0]
    id = message[1:]
    return int(id)

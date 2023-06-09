from dbase import get_prof_forview, get_prof_forsetting, get_description
from funcs.bdate_to_info import get_bdate_info
from funcs.purposes import get_purposes_from_list


async def generate_profile_forview(id, dist=None):
    profile = await get_prof_forview(id)
    bdate_info = await get_bdate_info(profile["bdate"])
    msg1 = f'{profile["name"]}, {bdate_info["age"]} (&#127380;{profile["id"]})\n'
    msg1 += f'{dist} км от тебя\n' if dist else ''
    if dist == 0:
        msg1 += f'0 км от тебя\n'
    msg1 += f'{profile["city"]}\n\nЦели:\n'
    purposes = await get_purposes_from_list(profile['purposes'])
    for purpose in purposes:
        msg1 += f'&#10004;{purpose}\n'
    main_photo = profile['main_photo']
    contacts = {'cont_vk': profile['cont_vk'], 'cont_tg': profile['cont_tg']}
    return {'msg1': msg1, 'm_ph': main_photo, 'contacts': contacts}


async def generate_profile_forsettings(tg_id):
    profile = await get_prof_forsetting(tg_id)
    if profile["find_f"] == 1 and profile["find_m"] == 1:
        findsex = 'девушек и парней'
    elif profile["find_f"] == 1:
        findsex = 'только девушек'
    elif profile["find_m"] == 1:
        findsex = 'только парней'
    msg1 = f'&#127380;{profile["id"]}\n' \
           f'Имя: {profile["name"]}\n' \
           f'Дата рождения: {profile["bdate"].strftime("%d.%m.%Y")}\n' \
           f'Город: {profile["city"]}\n' \
           f'Пол: {"мужской" if profile["sex"] == 2 else "женский"}\n' \
           f'Ты ищешь: {findsex}\n' \
           f'От {profile["age_min"]} до {profile["age_max"]} лет\n' \
           f'На расстоянии {profile["dist"]} км\n' \
           f'Цели:\n'
    purposes = await get_purposes_from_list(profile['purposes'])
    for purpose in purposes:
        msg1 += f'&#10004;{purpose}\n'
    msg2 = ''
    msg2 += f'Описание: {profile["description"]}\n' if profile["description"] else ''
    msg2 += f'\U0001F4CF {profile["height"]} см\n' if profile["height"] else ''
    msg2 += f'\U0001F4BC {profile["busy"]}\n' if profile["busy"] else ''
    msg2 += f'\U0001F466 {profile["children"]}\n' if profile["children"] else ''
    msg2 += f'\U0001F552 {profile["hobby"]}\n' if profile["hobby"] else ''
    msg2 += f'\U0001F6AB {profile["habits"]}\n' if profile["habits"] else ''
    msg2 += f'\U0001F436 {profile["animals"]}\n' if profile["animals"] else ''
    msg2 += 'Хочешь что-нибудь поменять?'
    att1 = profile['main_photo']
    att2 = profile['other_photos']
    return {'msg1': msg1, 'msg2': msg2, 'att1': att1, 'att2': att2}


async def get_id_from_message(message):
    message = message.split('(')[1]
    message = message.split(')')[0]
    id = message[1:]
    return int(id)


async def generate_profile_description(pr_id):
    description = await get_description(pr_id)
    bdate_info = await get_bdate_info(description["bdate"])
    msg = ''
    msg += f'{description["description"]}\n\n' if description["description"] else ''
    msg += f'\U0001F4CF {description["height"]} см\n' if description["height"] else ''
    msg += f'\U0001F4BC {description["busy"]}\n' if description["busy"] else ''
    msg += f'\U0001F466 {description["children"]}\n' if description["children"] else ''
    msg += f'\U0001F320 {bdate_info["zodiac"]}\n'
    msg += f'\U0001F552 {description["hobby"]}\n' if description["hobby"] else ''
    msg += f'\U0001F6AB {description["habits"]}\n' if description["habits"] else ''
    msg += f'\U0001F436 {description["animals"]}' if description["animals"] else ''
    return msg

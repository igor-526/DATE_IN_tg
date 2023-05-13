from models import Settings
from dbase.tgtoid import get_profile_id


async def dates_info(tg_id):
    prof_id = await get_profile_id(tg_id)
    settings = await Settings.query.where(Settings.profile_id == prof_id).gino.first()
    return {'created': settings.created, 'last_usage': settings.last_usage, 'deactivated': settings.deactivated,
            'name': settings.ch_name, 'sex': settings.ch_sex, 'bdate': settings.ch_bdate}
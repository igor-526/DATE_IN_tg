from models import Profile, Settings
from datetime import datetime


async def get_profile_id(tg_id):
    profile = await Profile.query.where(Profile.tg_id == tg_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == profile.id).gino.first()
    await settings.update(last_usage=datetime.now()).apply()
    return profile.id

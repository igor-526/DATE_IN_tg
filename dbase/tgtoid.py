from models import Profile

async def get_profile_id(tg_id):
    profile = await Profile.query.where(Profile.tg_id == tg_id).gino.first()
    return profile.id

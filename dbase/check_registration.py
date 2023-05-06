from models import Profile


async def chk_reg(id):
    profile = await Profile.query.where(Profile.tg_id == id).gino.first()
    return profile


async def chk_vk_reg(id):
    profile = await Profile.query.where(Profile.id == id).gino.first()
    return profile

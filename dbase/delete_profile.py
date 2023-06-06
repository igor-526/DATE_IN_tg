from models import Profile, Images, Offerlist, Matchlist, Settings


async def del_profile(pr_id):
    profile = await Profile.query.where(Profile.id == pr_id).gino.first()
    settings = await Settings.query.where(Settings.profile_id == pr_id).gino.first()
    photos = await Images.query.where(Images.profile_id == pr_id).where(Images.description == 'profile_photo').gino.all()
    offers1 = await Offerlist.query.where(Offerlist.profile_id == pr_id).gino.all()
    offers2 = await Offerlist.query.where(Offerlist.offer_id == pr_id).gino.all()
    matches1 = await Matchlist.query.where(Matchlist.profile_1_id == pr_id).gino.all()
    matches2 = await Matchlist.query.where(Matchlist.profile_2_id == pr_id).gino.all()
    for item in photos:
        await item.delete()
    for item in offers1:
        await item.delete()
    for item in offers2:
        await item.delete()
    for item in matches1:
        await item.delete()
    for item in matches2:
        await item.delete()
    await settings.delete()
    await profile.delete()

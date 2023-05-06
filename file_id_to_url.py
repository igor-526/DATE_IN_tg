file_id = event['photo'][-1]['file_id']
file_path = await bot.get_file(file_id)
url = bot.get_file_url(file_path['file_path'])
print(url)
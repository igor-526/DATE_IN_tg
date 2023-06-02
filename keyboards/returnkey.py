from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Восстановить")

return_keys = ReplyKeyboardMarkup(resize_keyboard=True)
return_keys.add(b1)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

async def start_menu_btn():
  btn = ReplyKeyboardMarkup(resize_keyboard=True)
  btn.row("🍴menyu")
  btn.row("🛍mening buyurtmalarim")
  btn.row("✍️ Fikr bildirish", "⚙️ Sozlamalar")

  return btn

async def wtart_menu_btn():
  btn  = ReplyKeyboardMarkup(resize_keyboard=True)
  btn.row("🗺️mening manzillarim")
  btn.row(KeyboardButton("📍geolokatsiya yuborish", request_location=True),"🔙orqaga")

  return btn



async def  art_menu_btn():
  btn = ReplyKeyboardMarkup(resize_keyboard=True)
  btn.row("📞mening raqamim","🔙orqaga")

  return btn


import logging
from  aiogram import Bot,Dispatcher,executor,types
from aiogram.types import *
from  btns import *


logging.basicConfig(level=logging.INFO)
BOT_TOKEN ="5986908987:AAF8UUsCooH7SCW07FPLcxzJfxpIWlzwIB8"


bot = Bot(token=BOT_TOKEN,parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_bot(message:types.Message):
    btn = await start_menu_btn()
    await message.answer("Quyidagilardan birini tanlang",reply_markup=btn)


@dp.message_handler(text="🍴menyu")
async def start_bot(message:types.Message):
    g = await wtart_menu_btn()
    await message.answer("Quyidagilardan birini tanlang",reply_markup=g)




@dp.message_handler(text="🔙orqaga")
async def start_bot(message:types.Message):
    btn = await start_menu_btn()
    await message.answer("Quyidagilardan birini tanlang",reply_markup= btn)


@dp.message_handler(text="🛍mening buyurtmalarim")
async def start_bot(message:types.Message):
    await message.answer("siz hech qana ovqat buyurtma qilmagansiz")



@dp.message_handler(text="✍️ Fikr bildirish")
async def start_bot(message:types.Message):
    o = await art_menu_btn()
    await message.answer("Siz bilan keyingi muloqot uchun kontaktni baham ko'ring",reply_markup=o)

if  __name__ == "__main__":
    executor.start_polling(dp)
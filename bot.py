import asyncio 
from aiogram import Bot, Dispatcher, types 
from aiogram.types import Message 
from aiogram.filters import Command 
from api import TOKEN
  
bot = Bot(token=TOKEN) 
dp = Dispatcher() 
 
@dp.message(Command("start")) 
async def send_welcome(message: Message): 
    await message.answer("Привет! Я твой Telegram-бот ⚡") 

@dp.message(Command("help"))
async def send_help(message: Message):
    await message.answer("Я умею писать команды /start и /help.")
 
async def main(): 
    print("Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) 
 
if _name_ == "_main_": 
    asyncio.run(main())
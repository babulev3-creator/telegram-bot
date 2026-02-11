import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8473713905:AAFXqsCRyd9Fpg0PnBvIKm02CaKIu7TEOx0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def handle_join_request(request: ChatJoinRequest):
    user_id = request.from_user.id

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Подать заявку в Канал 1", url="https://t.me/+ССЫЛКА2")],
        [InlineKeyboardButton(text="Подать заявку в Канал 2", url="https://t.me/+ССЫЛКА3")]
    ])

    await bot.send_photo(
        user_id,
        photo="https://via.placeholder.com/500x300.png",
        caption="Ваша заявка получена ✅\n\nПока вы ждёте одобрения, можете подать заявки в другие каналы 👇",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

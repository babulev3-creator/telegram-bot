import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton

# 🔹 1. ВСТАВЬ СЮДА ТОКЕН ИЗ BotFather
TOKEN = "8576393002:AAGBZZNH3RN7UIrsgeeDOdVHOBcGM5pjLxY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.chat_join_request()
async def handle_join_request(request: ChatJoinRequest):
    user_id = request.from_user.id

    # 🔹 2. ВСТАВЬ СЮДА ССЫЛКИ НА ДРУГИЕ КАНАЛЫ
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Подать заявку в Канал 2",
            url="https://t.me/+xrNyRhUwFVlmNmMy"  # ← заменить
        )],
        [InlineKeyboardButton(
            text="Подать заявку в Канал 3",
            url="https://t.me/+8B7ySuUtoM03YTky"  # ← заменить
        )]
    ])

    await bot.send_photo(
        user_id,

        # 🔹 3. СЮДА МОЖНО ВСТАВИТЬ СВОЮ ССЫЛКУ НА КАРТИНКУ
        photo="https://i.ibb.co/ksFMrbSN/5976770502665636842.jpg",

        # 🔹 4. СЮДА ПИШЕШЬ СВОЙ ТЕКСТ
        caption="Ваша заявка получена ✅\n\n"
                "Пока вы ждёте одобрения, можете подать заявки в другие каналы 👇",

        reply_markup=keyboard
    )

    # ❗ ВАЖНО: НЕТ автоматического одобрения
    # Заявка останется висеть, ты принимаешь вручную

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

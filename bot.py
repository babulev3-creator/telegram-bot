import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton

# 🔹 1. ВСТАВЬ СЮДА ТОКЕН
TOKEN = "ТУТ_ТВОЙ_ТОКЕН"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.chat_join_request()
async def handle_join_request(request: ChatJoinRequest):
    user_id = request.from_user.id

    # 🔹 КНОПКИ
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Подать заявку в Канал 2",
            url="https://t.me/+xrNyRhUwFVlmNmMy"
        )],
        [InlineKeyboardButton(
            text="Подать заявку в Канал 3",
            url="https://t.me/+8B7ySuUtoM03YTky"
        )]
    ])

    # 🔹 ПЕРВОЕ СООБЩЕНИЕ (с картинкой)
    await bot.send_photo(
        user_id,
        photo="https://i.ibb.co/ksFMrbSN/5976770502665636842.jpg",
        caption=(
            "⚡️ СУНДУК КОРОЛЯ БЕСПЛАТНО ⚡️\n\n"
            "‼️ ПОЛУЧИ ПРЯМО СЕЙЧАС ‼️\n\n"
            "ВЫПОЛНЯЙ ЗАДАНИЯ НИЖЕ ЗА 3 СЕКУНДЫ И ЗАБИРАЙ 👇\n\n"
            "⬇️⬇️⬇️⬇️"
        ),
        reply_markup=keyboard
    )

    # 🔥 ЖДЁМ 30 СЕКУНД
    await asyncio.sleep(30)

    # 🔹 ВТОРОЕ СООБЩЕНИЕ
    await bot.send_message(
        user_id,
        "⬆️⬆️⬆️⬆️\n"
        "ТЫ УЖЕ УСПЕЛ ЗАБРАТЬ СУНДУК??\n\n"
        "У ТЕБЯ ОСТАЛАСЬ 1 МИНУТА ИЛИ ОН СГОРИТ!!\n\n"
        "ВЫПОЛНЯЙ ЗАДАНИЯ ЗА 3 СЕКУНДЫ И ЗАБИРАЙ 👆"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

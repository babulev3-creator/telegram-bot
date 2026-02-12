import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton

# 🔹 ВСТАВЬ СВОЙ ТОКЕН
TOKEN = "ТУТ_ТВОЙ_ТОКЕН"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.chat_join_request()
async def handle_join_request(request: ChatJoinRequest):
    user_id = request.from_user.id

    # 🔹 КНОПКИ
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎁 Подать заявку в Канал 2",
                url="https://t.me/+xrNyRhUwFVlmNmMy"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔥 Подать заявку в Канал 3",
                url="https://t.me/+8B7ySuUtoM03YTky"
            )
        ]
    ])

    # 🔹 ПЕРВОЕ СООБЩЕНИЕ (С КАРТИНКОЙ)
    await bot.send_photo(
        user_id,
        photo="https://i.ibb.co/ksFMrbSN/5976770502665636842.jpg",
        caption=(
            "⚡ <b>СУНДУК КОРОЛЯ БЕСПЛАТНО</b> ⚡\n\n"
            "‼️ <b>ПОЛУЧИ ПРЯМО СЕЙЧАС</b> ‼️\n\n"
            "ВЫПОЛНЯЙ ЗАДАНИЯ НИЖЕ ЗА <b>3 СЕКУНДЫ</b> И ЗАБИРАЙ 👇\n\n"
            "⬇️⬇️⬇️⬇️"
        ),
        parse_mode="HTML",
        reply_markup=keyboard
    )

    # 🔥 ЖДЁМ 30 СЕКУНД
    await asyncio.sleep(30)

    # 🔹 ВТОРОЕ СООБЩЕНИЕ (ЭФФЕКТ СРОЧНОСТИ)
    await bot.send_message(
        user_id,
        "⬆️⬆️⬆️⬆️\n\n"
        "<b>ТЫ УЖЕ УСПЕЛ ЗАБРАТЬ СУНДУК??</b>\n\n"
        "⏳ У ТЕБЯ ОСТАЛАСЬ <b>1 МИНУТА</b> ИЛИ ОН СГОРИТ!!\n\n"
        "⚡ ВЫПОЛНЯЙ ЗАДАНИЯ ЗА <b>3 СЕКУНДЫ</b> И ЗАБИРАЙ 👆",
        parse_mode="HTML"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


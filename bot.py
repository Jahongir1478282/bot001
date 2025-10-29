import asyncio
import logging, sys
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# Token olish va tekshirish
BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN muhit o'zgaruvchisida topilmadi!")

# Bot va Dispatcher
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """Start buyrug'ini qayta ishlash"""
    await message.answer("Salom! Bot ishlayapti ✅")


@dp.message()
async def echo(message: Message) -> None:
    """Barcha xabarlarni qayta ishlash"""
    if message.text:
        await message.answer(f"Siz yozdingiz: {message.text}")


async def main() -> None:
    """Botni ishga tushirish"""
    logger.info("Bot ishga tushmoqda...")
    try:
        await dp.start_polling(bot)  # type: ignore
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())

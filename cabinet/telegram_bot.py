import logging

import telegram
from django.conf import settings

logging.basicConfig(level=logging.DEBUG)


async def send_to_telegram(message, parse_mode="Markdown"):
    try:
        bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)

        await bot.send_message(
            chat_id=settings.TELEGRAM_CHAT_ID,
            text=message,
            parse_mode=parse_mode
        )
        logging.info(
            f'Сообщение "{message}" '
            f'отправлено в чат {settings.TELEGRAM_CHAT_ID}'
        )
    except Exception as err_msg:
        logging.error(
            "Ошибка отправки сообщения в чат "
            f"{settings.TELEGRAM_CHAT_ID}: {err_msg}"
        )
        raise

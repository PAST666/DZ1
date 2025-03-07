import asyncio

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from cabinet.models import Visit
from cabinet.telegram_bot import send_telegram_message


@receiver(post_save, sender=Visit)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        message = (
            "*Новая запись на консультацию*"
            f"*Имя:* {instance.name}"
            f"*Телефон:* {instance.phone or 'не указан'}"
            f"*Комментарий:* {instance.comment or 'не указан'}"
            f"{'-' * 30}"
        )
        asyncio.run(send_telegram_message(
            settings.TELEGRAM_BOT_TOKEN,
            settings.TELEGRAM_CHAT_ID,
            message)
        )

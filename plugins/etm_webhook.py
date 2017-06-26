"""
extend with webhook
"""
# coding=utf-8
from plugins.eh_telegram_master import TelegramChannel
import config

class ETM_Webhook(TelegramChannel):
    def polling_from_tg(self):
        """
        copy from
        https://github.com/RoyXiang/ehForwarderBot/commit/dc43f8106535d3f6576ab6597864a12a9b7bdc1b
        """
        webhook_url = getattr(config, 'webhook_url', default='')
        if webhook_url != '':
            token = getattr(config, self.channel_id)['token']
            self.bot.start_webhook(listen='0.0.0.0', port=5002, url_path=token)
            if not webhook_url.endswith('/'):
                webhook_url += '/'
            webhook_url += token
            self.bot.bot.setWebhook(webhook_url=webhook_url)
        else:
            self.bot.start_polling(timeout=10)

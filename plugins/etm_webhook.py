from plugins.eh_telegram_master import TelegramChannel
import config

class ETM_Webhook(TelegramChannel):
    def polling_from_tg(self):
        webhook_url = ''
        token = getattr(config, self.channel_id)['token']
        self.bot.start_webhook(listen='0.0.0.0', port=5002, url_path=token)
        webhook_url += token
        self.bot.bot.setWebhook(webhook_url=webhook_url)
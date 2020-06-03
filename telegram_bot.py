import telegram
from telegram.ext import Updater, CommandHandler

class MyBot:
    def __init__(self, token):
        self.bot = telegram.Bot(token)
        self.updater = Updater(token)

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.updater.start_polling()
        self.updater.idle()


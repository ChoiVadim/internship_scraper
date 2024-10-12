from telebot import TeleBot
from telebot import apihelper
from tgbot.filters.admin_filter import AdminFilter
from tgbot.handlers.admin import admin_user
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import any_user
from tgbot.middlewares.antiflood_middleware import antispam_func
from tgbot.states.register_state import Register
from tgbot.utils.database import Database
from tgbot import config

apihelper.ENABLE_MIDDLEWARE = True


db = Database()
bot = TeleBot(config.TOKEN, num_threads=5)


def register_handlers():
    bot.register_message_handler(
        admin_user, commands=["start"], admin=True, pass_bot=True
    )
    bot.register_message_handler(
        any_user, commands=["start"], admin=False, pass_bot=True
    )
    bot.register_message_handler(anti_spam, commands=["spam"], pass_bot=True)


register_handlers()
bot.register_middleware_handler(antispam_func, update_types=["message"])
bot.add_custom_filter(AdminFilter())


def run():
    bot.infinity_polling()


if __name__ == "__main__":
    run()

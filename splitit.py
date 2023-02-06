import logging

import aiogram

from singletons.bot import Bot
from singletons.config import Config


def main():
    logging.basicConfig(level=logging.DEBUG if Config()["DEBUG"] else logging.INFO)
    Bot(Config()["6089522865:AAG0vUsYSBg-BaSfiG1T5E1QTrorjoMDA4U"])
    from bot import start
    from bot import splitit
    aiogram.executor.start_polling(Bot().dispatcher, skip_updates=True)


if __name__ == '__main__':
    main()

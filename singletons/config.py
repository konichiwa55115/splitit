from typing import Any, Dict

from decouple import config

from utils.singleton import singleton


@singleton
class Config:
    def __init__(self):
        self._config: Dict[str, Any] = {
            "DEBUG": config("DEBUG", default="0", cast=bool),
            "TELEGRAM_API_TOKEN": "6089522865:AAG0vUsYSBg-BaSfiG1T5E1QTrorjoMDA4U"
        }

    def __getitem__(self, item: str) -> Any:
        return self._config[item]

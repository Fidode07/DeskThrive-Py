import json
import os.path


class ConfigHelper:
    def __init__(self, config_path: str) -> None:
        self.__config_path: str = config_path
        self.__config: dict = self.__load_config()

    def __load_config(self) -> dict:
        if not os.path.isfile(self.__config_path):
            with open(self.__config_path, 'w') as f:
                default_settings: dict = {
                    'host': '0.0.0.0',
                    'q_host': 'localhost',
                    'port': 2030,
                    'ui_title': 'DeskThrive',
                    'ui_width': 1200,
                    'ui_height': 700,
                    'icon_path': 'src/img/DeskThriveIcon.png'
                }
                json.dump(default_settings, f, indent=4)
        with open(self.__config_path, 'r') as f:
            return json.load(f)

    def get_setting(self, setting: str) -> str:
        return self.__config[setting]

    def set_setting(self, setting: str, value: str) -> None:
        self.__config[setting] = value
        with open(self.__config_path, 'w') as f:
            json.dump(self.__config, f, indent=4)

import webview

from ext.utils import ConnectionInformation
from ext.config_helper import ConfigHelper


class ExternUiHelper:
    @staticmethod
    def start(config_helper: ConfigHelper, background_server_info: ConnectionInformation) -> None:
        ui: Ui = Ui(config_helper=config_helper, background_server_info=background_server_info)
        ui.start()


class Ui:
    def __init__(self, config_helper: ConfigHelper, background_server_info: ConnectionInformation) -> None:
        self.__config_helper: ConfigHelper = config_helper
        self.__connection_info: ConnectionInformation = background_server_info
        self.__ui: webview.Window = self.__create_ui()

    def __create_ui(self) -> webview.Window:
        title: str = self.__config_helper.get_setting('ui_title')
        width: int = int(self.__config_helper.get_setting('ui_width'))
        height: int = int(self.__config_helper.get_setting('ui_height'))

        ui: webview.Window = webview.create_window(title=title, url='src/index.html', width=width, height=height)
        return ui

    @staticmethod
    def start() -> None:
        webview.start(http_server=False)

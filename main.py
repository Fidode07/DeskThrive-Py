from multiprocessing import Process
from ext.config_helper import ConfigHelper
from ext.background_helper import BackgroundHelper, ExternBackgroundHelper
from ext.ui_helper import Ui, ExternUiHelper
from ext.utils import ConnectionInformation
from ext.tray_helper import ExternTrayIconHelper


def main() -> None:
    config_helper: ConfigHelper = ConfigHelper(config_path='config.json')

    # get host and port to listen on
    host, port = str(config_helper.get_setting('q_host')), int(config_helper.get_setting('port'))
    connection_info: ConnectionInformation = ConnectionInformation(host=host, port=port)

    is_background_server_running: bool = BackgroundHelper.is_background_server_running(connection_info=connection_info)
    ui: Ui = Ui(config_helper=config_helper, background_server_info=connection_info)

    if is_background_server_running:
        # if background server is running, start the UI
        ui.start()
        exit(0)

    # if background server is not running, start it
    background_server_process: Process = Process(target=ExternBackgroundHelper.start, args=(connection_info,))
    ui_process: Process = Process(target=ExternUiHelper.start, args=(config_helper, connection_info))
    tray_process: Process = Process(target=ExternTrayIconHelper.start, args=(config_helper.get_setting('icon_path'),))

    background_server_process.start()
    ui_process.start()
    tray_process.start()


if __name__ == '__main__':
    main()

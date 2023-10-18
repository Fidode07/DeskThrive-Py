import pystray
from PIL import Image


class ExternTrayIconHelper:
    @staticmethod
    def start(icon_path: str) -> None:
        tray_icon: TrayIcon = TrayIcon(icon_path=icon_path)
        tray_icon.start()


class TrayIcon:
    def __init__(self, icon_path: str):
        self.icon_path = icon_path
        self.icon_image = Image.open(icon_path)
        self.tray_icon = self.create_tray_icon()

    def quit(self) -> None:
        self.tray_icon.stop()
        # TODO: Send background_server a message to stop

    def create_tray_icon(self) -> pystray.Icon:
        menu = pystray.Menu(
            pystray.MenuItem(
                text='Quit',
                action=self.quit
            )
        )
        return pystray.Icon(
            name='DeskThrive',
            title='DeskThrive',
            icon=self.icon_image,
            menu=menu
        )

    def start(self):
        self.tray_icon.run()

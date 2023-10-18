import socket
from ext.utils import ConnectionInformation
from typing import *


class ExternBackgroundHelper:
    @staticmethod
    def start(connection_info: ConnectionInformation) -> None:
        background_helper: BackgroundHelper = BackgroundHelper(connection_info=connection_info)
        background_helper.start()


class BackgroundHelper:
    @staticmethod
    def is_background_server_running(connection_info: ConnectionInformation, timeout: float = .5) -> bool:
        sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((connection_info.host, connection_info.port))
            sock.shutdown(socket.SHUT_RDWR)
            return True
        except socket.error:
            return False
        finally:
            sock.close()

    def __init__(self, connection_info: ConnectionInformation) -> None:
        self.__connection_info: ConnectionInformation = connection_info
        self.__server: socket.socket = self.__create_server()

    def __create_server(self) -> socket.socket:
        server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.__connection_info.host, self.__connection_info.port))
        server.listen(1)
        return server

    def start(self) -> None:
        while True:
            conn, addr = self.__server.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    # TODO: handle data

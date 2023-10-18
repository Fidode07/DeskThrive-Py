from dataclasses import dataclass


@dataclass
class ConnectionInformation:
    host: str
    port: int

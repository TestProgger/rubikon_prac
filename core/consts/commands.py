from enum import Enum


class ProtocolTypes(str, Enum):
    FTP = 'ftp'
    SMB = 'smb'


PROTOCOL_CHOICES = (
    ProtocolTypes.FTP.value,
    ProtocolTypes.SMB.value
)


class NetworkPort(Enum):
    MIN_PORT = 1
    MAX_PORT = 65535

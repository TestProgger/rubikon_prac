import argparse
from core.consts import commands
from core.types.parsers import argument_type_parser
from core.workers.ftp import FTPWorker
from core.workers.smb import SMBWorker
import logging
from smbprotocol.connection import Dialects

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)


parser = argparse.ArgumentParser(
    description="Exploiter"
)

parser.add_argument(
    '-t', '--type',
    choices=commands.PROTOCOL_CHOICES,
    required=True,
    help="Протокол"
)

parser.add_argument(
    '-u', '--user',
    type=str,
    help="Имя пользователя",
)

parser.add_argument(
    '-p', '--password',
    type=str,
    help="Пароль пользователя"
)

parser.add_argument(
    '--host',
    type=str,
    required=True,
    help="Хост"
)

parser.add_argument(
    '--port',
    type=argument_type_parser.port,
    default=21,
    help="Порт"
)

parser.add_argument(
    '--timeout',
    type=int,
    default=60,
    help="Таймаут ответа"
)

parser.add_argument(
    '--use-tls',
    action=argparse.BooleanOptionalAction,
    type=bool,
    default=False,
    help="Использовать протокол TLS при подключении"
)

if __name__ == '__main__':
    args = parser.parse_args()
    if args.type == commands.ProtocolTypes.FTP.value:
        FTPWorker(**args.__dict__).run()
    else:
        SMBWorker(**args.__dict__).run()
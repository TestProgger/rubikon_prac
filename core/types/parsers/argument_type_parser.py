import argparse
from core.consts import commands
from urllib import parse as urllib_parse
def port(arg: str):
    try:
        port = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError('Порт должен быть положительным целочисленным значением')

    if commands.NetworkPort.MIN_PORT.value > port:
        raise argparse.ArgumentTypeError(f"Порт не может быть меньше {commands.NetworkPort.MIN_PORT.value}")

    if commands.NetworkPort.MAX_PORT.value < port:
        raise argparse.ArgumentTypeError(f"Порт не может быть больше {commands.NetworkPort.MAX_PORT.value}")

    return port


def host(arg: str):
    parsed_url = urllib_parse.urlparse(arg)
    if parsed_url.scheme and parsed_url.netloc:
        return urllib_parse.urlunparse(parsed_url)

    if parsed_url.path:
        return parsed_url.path

    raise argparse.ArgumentTypeError('Невалидное имя хоста')
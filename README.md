# rubikon_prac

1. Установка зависимостей
 ```bash 
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt 
```

2. Описание параметров командной строки
```bash
usage: main.py [-h] -t {ftp,smb} [-u USER] [-p PASSWORD] --host HOST [--port PORT] [--timeout TIMEOUT] [--use-tls | --no-use-tls]

Exploiter

options:
  -h, --help            show this help message and exit
  -t {ftp,smb}, --type {ftp,smb}
                        Протокол
  -u USER, --user USER  Имя пользователя
  -p PASSWORD, --password PASSWORD
                        Пароль пользователя
  --host HOST           Хост
  --port PORT           Порт
  --timeout TIMEOUT     Таймаут ответа
  --use-tls, --no-use-tls
                        Использовать протокол TLS при подключении
```


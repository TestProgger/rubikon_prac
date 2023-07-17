import pydantic
from typing import Optional
import ftplib
from core.utils import decorators
import logging

logger = logging.getLogger(__name__)


class FTPWorkerParams(pydantic.BaseModel):
    host: str
    user: Optional[str] = None
    password: Optional[pydantic.PositiveInt] = None
    port: Optional[int] = 21
    timeout: Optional[pydantic.PositiveInt] = 60
    use_tls: Optional[bool] = False


class FTPWorker:
    dir_result: list[str] = []
    pwd_result: str = None

    def __init__(self,  **kwargs: FTPWorkerParams):
        self.data = FTPWorkerParams(**kwargs)
        if self.data.use_tls:
            self.instance = ftplib.FTP_TLS(host=self.data.host)
        else:
            self.instance = ftplib.FTP(host=self.data.host)

    @decorators.log_method(logger)
    def run(self):
        if self.data.password and self.data.user:
            self._connect_with_credentials()
        else:
            self._connect_anonymous()

        return self.__format_result()

    @decorators.log_method(logger)
    def _connect_with_credentials(self):

        self.instance.connect(
            host=self.data.host,
            port=self.data.port,
            timeout=self.data.timeout
        )
        self.instance.login(
            user=self.data.user,
            passwd=self.data.password
        )

        self.pwd_result = self.instance.pwd()
        self.instance.dir(self.__set_dir_result)

    @decorators.log_method(logger)
    def _connect_anonymous(self):
        self.instance.connect(
            host=self.data.host,
            port=self.data.port
        )
        self.instance.login()
        self.pwd_result = self.instance.pwd()
        self.instance.dir(self.__set_dir_result)


    def __set_dir_result(self, result:str):
        self.dir_result.append(result)

    def __format_result(self):
        return (
            "Успешное подключение",
            f"Текущая директория {self.pwd_result}",
            f"Листинг директории",
            self.dir_result
        )



import smbclient
import pydantic
from typing import Optional
import logging
from core.utils import decorators
logger = logging.getLogger(__name__)

# SMB_DIALECTS = {key: value for key, value in Dialects.__dict__.items() if key.startswith('SMB_')}

class SMBWorkerParams(pydantic.BaseModel):
    host: str
    user: Optional[str] = None
    password: Optional[pydantic.PositiveInt] = '-N'
    timeout: Optional[int] = 60
    port: Optional[int] = 445


class SMBWorker:
    instance = None

    def __init__(self, **kwargs: SMBWorkerParams):
        self.data = SMBWorkerParams(**kwargs)

    @decorators.log_method(logger)
    def run(self):
        try:
            if self.data.user and self.data.password:
                self.instance = smbclient.register_session(
                    server=self.data.host,
                    port=self.data.port,
                    username=self.data.user,
                    password=self.data.password,
                    connection_timeout=self.data.timeout
                )
            else:
                self.instance = smbclient.register_session(
                    server=self.data.host,
                    port=self.data.port,
                    connection_timeout=self.data.timeout
                )
        except:
            pass

        if self.instance is None:
            logger.info(
                f"{self.__class__.__name__} | run | Ошибка подключения Полезная нагрузка: {self.data.model_dump(exclude_none=True)}"
            )
        else:
            logger.info(
                f"{self.__class__.__name__} | run | Успешное подключение Полезная нагрузка: {self.data.model_dump(exclude_none=True)}"
            )

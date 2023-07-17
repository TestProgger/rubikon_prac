import functools
import logging


def log_method(logger: logging.Logger, description: str = None):
    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(self, *args, **kwargs):
            payload = self.data.model_dump(exclude_none=True)
            logger.info(
                f"{self.__class__.__name__} | {description or func.__name__} | Полезная нагрузка: {payload}"
            )
            try:
                result = func(self, *args, **kwargs)
            except Exception as ex:
                logger.exception(
                    f"{self.__class__.__name__} | {description or func.__name__} | Ошибка: {str(ex)}"
                )
                return

            logger.info(f"{self.__class__.__name__} | {description or func.__name__} | Результат: {result}")

            return result
        return _wrapper
    return _decorator
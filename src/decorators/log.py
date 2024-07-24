# src/decorators/log.py
import functools
import logging
from typing import Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования начала и конца выполнения функции,
    ее результата или возникших ошибок.

    :param filename: Имя файла для логов. Если не задано, логирование в консоль.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
            handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
            formatter = logging.Formatter('%(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise
            finally:
                logger.removeHandler(handler)
                handler.close()
        return wrapper
    return decorator

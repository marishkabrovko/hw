import functools
import logging
import sys
from typing import Callable, Any, Optional

def log(filename: Optional[str] = None):
    def decorator_log(func: Callable) -> Callable:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.DEBUG)

        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator_log

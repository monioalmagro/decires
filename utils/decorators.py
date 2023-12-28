# Standard Libraries
import functools
import logging

# Third-party Libraries
from django.db import DatabaseError, IntegrityError

logger = logging.getLogger(__name__)


def mutation_exception_handler(log_tag: str):
    """
    Decorator that handles specific exceptions for asynchronous
    functions in Django.

    Parameters:
    - log_tag (str): Log tag used to identify log entries.

    Usage:
    @mutation_exception_handler("my_log_tag")
    async def my_async_function():
        # ...
    """

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            if not isinstance(log_tag, str):
                raise ValueError("log_tag debe ser una cadena")
            full_log_tag = f"{log_tag}.{func.__name__}"
            try:
                result = await func(*args, **kwargs)
                return result
            except AssertionError as exp:
                logger.warning(
                    f"*** {full_log_tag}, VALIDATION ERROR"
                    f" {str(exp)} - {repr(exp)}***",
                    exc_info=True,
                )
            except (DatabaseError, IntegrityError) as exp:
                logger.warning(
                    f"*** {full_log_tag}, INTEGRITY ERROR"
                    f" {str(exp)} - {repr(exp)}***",
                    exc_info=True,
                )
            except Exception as exp:
                logger.warning(
                    f"*** {full_log_tag}, INTERNAL ERROR"
                    f" {str(exp)} - {repr(exp)}***",
                    exc_info=True,
                )

        return wrapper

    return decorator

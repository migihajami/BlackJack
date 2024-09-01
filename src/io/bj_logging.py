import logging


def log_execution(f):
    def wrapper(*args, **kwargs):
        logging.debug(f"executing {f}")
        return f(*args, **kwargs)
    return wrapper


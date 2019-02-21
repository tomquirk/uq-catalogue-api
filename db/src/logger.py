import logging

_LOGGING_CONFIGURED = False


def get_logger(name):
    """
    Configure logging and return the logger for [name].

    Logging configuration is done once only the first time this method is called.
    """
    global _LOGGING_CONFIGURED
    if not _LOGGING_CONFIGURED:
        logging.basicConfig(level=logging.INFO)
        _LOGGING_CONFIGURED = True
    return logging.getLogger(name)

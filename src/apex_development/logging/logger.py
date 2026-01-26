import logging


def get_logger(service_name:str, level_logging: str=logging.INFO) -> logging.Logger:
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "plain": {
                "format": ("%(asctime)s "
                           "%(levelname)-5s "
                           "--- [%(name)-32s] "
                           f"[{service_name:<33}] "
                           "%(message)s"),
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "plain",
                "level": level_logging
            }
        },

        "root": {
            "handlers": ["console"],
            "level": level_logging
        }
    }

    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(service_name)
    return logger

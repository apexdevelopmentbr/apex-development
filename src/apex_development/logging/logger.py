import logging


def setup_log(level_logging: str) -> logging.Logger:
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "plain": {
                "format": ("%(asctime)s "
                           "%(levelname)-5s "
                           "--- [%(name)-32s]"
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

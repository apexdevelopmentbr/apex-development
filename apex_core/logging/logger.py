import logging

def setup_log(service_name:str, level_logging: str) -> logging.Logger:

    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "colored":{
              "()" : "colorlog.ColoredFormatter",
              "format": ("%(yellow)s %(asctime)s%(reset)s"
                "%(log_color)s %(levelname)-5s %(reset)s"
                "--- [%(name)-32s]"
                f"%(white)s [%(purple)s{service_name:<33}%(white)s] %(reset)s: "
                "%(message)s"),
                "log_colors": {
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "bold_red",
                },
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "colored",
                "level": level_logging
            }
        },

        "root": {
            "handlers": ["console"],
            "level": level_logging
        }
    }

    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    return logger


import logging
from logging.config import dictConfig
from config import Config

# Logging configuration
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s | %(asctime)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        f"{Config.app_name}": {
            "handlers": ["default"],
            "level": "DEBUG",  # Set your desired logging level here
        },
    },
}

# Configure logging
dictConfig(log_config)

# Define a logger
log = logging.getLogger(Config.app_name)

# Test logging
log.info(f"{Config.app_name} logger Initialize")
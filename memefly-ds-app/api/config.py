import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib
import os
import sys

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

FORMATTER = logging.Formatter(
        "%(asctime)s — %(name)s — %(levelname)s —"
        "%(funcName)s:%(lineno)d — %(message)s")

LOG_DIR = PACKAGE_ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'api.log'


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(logging.DEBUG)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(
            LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.WARNING)
    return file_handler


def get_logger(*, logger_name):
    """
    Get logger with prepared handlers.
    """
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False

    return logger


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SERVER_PORT = 8000


class ProductionConfig(Config):
    DEBUG = False
    SERVER_PORT = os.environ.get('PORT', 8000)


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    IMG_FEATURE_EXTRACTOR = "api/weights/inceptionv3_embeddings.h5"
    TOKENIZER = "api/weights/memefly-word-data-v2-tokenizer.pkl"
    MODEL = "api/weights/memefly-word-150-201912080317-50-10.24.h5"
    MAX_LENGTH = 150
    BUCKET_NAME = "memefly-datalake"
    REGION_NAME = "us-east2"
    IMG_FOLDER_NAME = "base_meme-images"
    S3_FOLDER = ""


class TestingConfig(Config):
    TESTING = True


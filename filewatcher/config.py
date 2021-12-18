from dotenv import load_dotenv
import os
from os.path import join, dirname

# Initialize env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# Base config
class BaseConfig:
    def __init__(self):
        pass

    TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN', None)
    TELEGRAM_API_URL = os.environ.get('TELEGRAM_API_URL', None)
    TELEGRAM_GROUP_ID = os.environ.get('TELEGRAM_GROUP_ID', None)

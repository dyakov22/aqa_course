import os
from .user_config import UserConfig

from .driver_config import driver_config


config_file_path = os.path.dirname(__file__)

print(config_file_path)
PLATFORM = os.getenv('PLATFORM', 'android')

config_d = driver_config(PLATFORM)

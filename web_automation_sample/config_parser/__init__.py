import os

from configparser import ConfigParser

path_to_dir = os.path.dirname(__file__)

path_to_config = os.path.join(path_to_dir, 'config_data.ini')

file = os.getenv('ENV_FILE', path_to_config)

config = ConfigParser()

config.read(file)

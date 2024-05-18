import logging.config

import pyscroll
import yaml

from . import lib
from . import app
from .app.definitions import LOGGING_LEVEL, ROOT_DIR

# Load Logger Config File
with open(f'{ROOT_DIR}\\conf\\logging_config.yaml', 'rt') as file:
    config = yaml.safe_load(file.read())

# Config Logger
logging.config.dictConfig(config)

# Get a Logger Object
logger = logging.getLogger(LOGGING_LEVEL)
pyscroll.orthographic.log = logger

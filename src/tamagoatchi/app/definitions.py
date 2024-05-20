# Constants
# DIR
import pathlib
import os

ROOT_DIR = pathlib.Path(os.path.dirname(__file__))
GUI_EXECUTION = True
MAP_SIZE = (256, 144)
ROOT_SIZE = (1024, 576)
RATIO = 16 / 9
LOGGING_LEVEL = 'staging'

# Tamagotchi
NUMBER_OF_TAMAGOTCHI = 5  # Represent the number of tamagotchi at start
CARACTERISTICS_INITIAL_VALUE = 200
NOT_PRINTABLE_KEYS = 2  # Represent the number of keys weren't appear when we get tamagotchi status

# Game
DAY_DURATION = 60  # Number of second that the one day durate

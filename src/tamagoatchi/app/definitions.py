
import optparse
import pathlib
import os

# Make ArgParser for command line
option_parser = optparse.OptionParser()
option_parser.add_option('-g', dest="gui", action='store_true')
(options, args) = option_parser.parse_args()


# Constants
# DIR
ROOT_DIR = pathlib.Path(os.path.dirname(__file__))
if options.gui:
    GUI_EXECUTION = True
else:
    GUI_EXECUTION = False
MAP_SIZE = (256, 144)
ROOT_SIZE = (1024, 576)
RATIO = 16 / 9
LOGGING_LEVEL = 'production'

# Tamagotchi
NUMBER_OF_TAMAGOTCHI = 5  # Represent the number of tamagotchi at start
CARACTERISTICS_INITIAL_VALUE = 200
NOT_PRINTABLE_KEYS = 2  # Represent the number of keys weren't appear when we get tamagotchi status

# Game
DAY_DURATION = 90  # Number of second that the one day durate

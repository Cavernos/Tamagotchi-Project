from optparse import OptionParser

import keyboard
from Player import Player


class Main:
    def __init__(self) -> None:
        pass


    def launch(self):
        usage = "%prog [Argument] arg1 arg2"
        parser = OptionParser(usage=usage, add_help_option=False)
        parser.add_option("-h", "--help", action='help', help="Afficher les informations d'utilisation")
        parser.add_option(
            "-g", "--gui", help="Afficher le GUI", action="callback", callback=self.gui)
        parser.set_description("hello")
        (options, args) = parser.parse_args()

    def gui(self, option, opt, value, parser):
        print("parser.usage")


if __name__ == "__main__":
    Main().launch()


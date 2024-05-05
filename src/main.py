import logging
from optparse import OptionParser

import keyboard
from models.player import Player
from console import Console


class Main:
    def __init__(self) -> None:
        self.parser = OptionParser(usage="%prog [Argument] arg1 arg2", add_help_option=False)
        self.parser.add_option("-h", "--help", action='help', help="Afficher les informations d'utilisation")
        
        self.parser.add_option(
            "-g", "--gui", help="Afficher le GUI", action="callback", callback=self.gui)
        
        self.parser.add_option("-d", "--debug", help="Affiche les options de debug", dest="debug", action="store")
        self.parser.set_description("hello")
        self.options, self.args = self.parser.parse_args()

    def launch(self):
        if self.options.debug is not None:
            logging.basicConfig(level=self.options.debug.upper())
        self.console()

    def gui(self, option, opt, value, parser):
        pass
    
    def console(self):
        console = Console()
        console.start()


if __name__ == "__main__":
    Main().launch()

from os import system

import pygame, optparse

from tamagoatchi.app.definitions import ROOT_SIZE
from tamagoatchi.lib.event import EventHandler
from tamagoatchi.lib.handlers import ResourceHandler
from tamagoatchi.lib.view import ViewHandler


def main_cli():
    """
    Main class that initialize first view
    """
    view_handler = ViewHandler()
    while True:
        if view_handler.render() == -1:
            break
        view_handler.update()
        system('cls')


def main_gui():
    pygame.init()
    pygame.display.set_mode(ROOT_SIZE, pygame.RESIZABLE)
    icon_path = ResourceHandler.get_resources_location() + '\\tamagotchis\\default.png'
    icon = pygame.image.load(icon_path)
    pygame.display.set_icon(icon)
    pygame.display.set_caption('TamaGOATchi')
    running = True
    view_handler = ViewHandler()
    while running:
        if view_handler.render() == -1:
            break
        view_handler.update()
        for event in pygame.event.get():
            EventHandler.notify(event)
        pygame.display.flip()


if __name__ == '__main__':
    main_gui()
    option_parser = optparse.OptionParser()
    option_parser.add_option('-g', dest="gui", action='store_true')
    (options, args) = option_parser.parse_args()
    if options.gui:
        main_gui()
    else:
        main_cli()

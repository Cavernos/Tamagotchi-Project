import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame, optparse

from tamagoatchi.app.definitions import ROOT_SIZE, GUI_EXECUTION
from tamagoatchi.lib.event import EventManager
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
        os.system('cls')


def main_gui():
    """
    Define all pygame init tools
    Run Main loop and wait for events
    """
    pygame.init()
    pygame.display.set_mode(ROOT_SIZE, pygame.RESIZABLE)
    icon_path = os.path.join(ResourceHandler.get_resources_location(), 'tamagotchis', 'default.png')
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
            EventManager.from_id("Button Manager").notify(event)
            EventManager.from_id("View Manager").notify(event)
            EventManager.from_id("Key Manager").notify(event)
        pygame.display.flip()


def main():
    if GUI_EXECUTION:
        main_gui()
    else:
        main_cli()


if __name__ == '__main__':
    main()

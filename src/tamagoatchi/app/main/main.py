from os import system

import pygame, optparse

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
    screen = pygame.display.set_mode((1920, 1080))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("purple")
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    option_parser = optparse.OptionParser()
    option_parser.add_option('-g', dest="gui", action='store_true')
    (options, args) = option_parser.parse_args()
    if options.gui:
        main_gui()
    else:
        main_cli()

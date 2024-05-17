from os import system

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


if __name__ == '__main__':
    main_cli()

from os import system

from lib.view import ViewHandler

if __name__ == '__main__':
    view_handler = ViewHandler()
    while True:
        if view_handler.render() == -1:
            break
        view_handler.update()
        system('cls')

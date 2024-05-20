from tamagoatchi.app.gui.controllers.HomeController import *
from tamagoatchi.app.gui.controllers.GameController import *
# Dictionary of called controllers
__calledControllers = {}


def call_controller(name: str, method: str, request: Request):
    """
    Function that call a controller and a method
    """
    try:
        tmp = __calledControllers[name]
    except KeyError:
        tmp = __calledControllers[name] = globals()[name]()
    return getattr(tmp, method)(request)
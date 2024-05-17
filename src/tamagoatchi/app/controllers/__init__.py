from tamagoatchi.lib.communication import Request
from tamagoatchi.app.controllers.HomeController import *
from tamagoatchi.app.controllers.GameController import *
from tamagoatchi.app.controllers.GamePersonalizeController import *

# Dictionnary of called controllers
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

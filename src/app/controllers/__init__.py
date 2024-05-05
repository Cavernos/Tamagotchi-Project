from lib.communication import Request
from app.controllers.HomeController import *
from app.controllers.GameController import *
from app.controllers.GamePersonalizerController import *

__calledControllers = {}


def call_controller(name: str, method: str, request: Request):
    try:
        tmp = __calledControllers[name]
    except KeyError:
        tmp = __calledControllers[name] = globals()[name]()
    return getattr(tmp, method)(request)

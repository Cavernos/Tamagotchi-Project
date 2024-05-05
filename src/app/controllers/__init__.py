from lib.communication import Request
from app.controllers import *

__calledControllers = {}


def call_controller(name: str, method: str, request: Request):
    try:
        tmp = __calledControllers[name]
    except:
        tmp = __calledControllers[name] = globals()[name]()
    return getattr(tmp, method)(request)
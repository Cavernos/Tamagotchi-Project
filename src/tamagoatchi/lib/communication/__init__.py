from tamagoatchi.lib.communication.Request import *
from tamagoatchi.lib.communication.Response import *
from tamagoatchi.lib.communication.Router import *

from tamagoatchi.app.routes.Routes import get_routes

__router_instance = None


def get_router() -> Router:
    global __router_instance
    if __router_instance is None:
        __router_instance = Router(get_routes())
    return __router_instance

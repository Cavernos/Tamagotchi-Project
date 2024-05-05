from lib.communication.Request import *
from lib.communication.Response import *
from lib.communication.Router import *

from app.routes.Routes import get_routes

__router_instance = None


def get_router() -> Router:
    global __router_instance
    if __router_instance is None:
        __router_instance = Router(get_routes())
    return __router_instance

from tamagoatchi.lib.communication.Request import *
from tamagoatchi.lib.communication.Response import *
from tamagoatchi.lib.communication.Router import *

from tamagoatchi.app.routes.Routes import get_cli_routes

# Variable that contains a Router
__router_instance = None


def get_router() -> Router:
    # get Router instance
    global __router_instance
    if __router_instance is None:
        __router_instance = Router(get_cli_routes())
    return __router_instance

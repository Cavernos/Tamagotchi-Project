from pygame import Surface, SurfaceType

from tamagoatchi.lib.view import GUIView


class TamagotchiView(GUIView):
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        super().__init__(screen, ext_dict)
        self.view_location = ""

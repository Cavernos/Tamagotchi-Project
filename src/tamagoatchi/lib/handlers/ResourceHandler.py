import os

from tamagoatchi import ROOT_DIR


class ResourceHandler:
    """
    Class that define some utils method to get ressources
    """
    @staticmethod
    def get_resources_location() -> str:
        """
        Method to get assets folder location folder
        """
        return os.path.join(str(ROOT_DIR.parent), "assets")

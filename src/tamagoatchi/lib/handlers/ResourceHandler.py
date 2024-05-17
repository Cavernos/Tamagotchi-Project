from tamagoatchi import ROOT_DIR


class ResourceHandler:
    @staticmethod
    def get_resources_location() -> str:
        return str(ROOT_DIR.parent) + "\\assets"

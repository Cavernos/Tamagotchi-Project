from tamagoatchi.lib.communication import Request
from tamagoatchi.lib.handlers import SaveHandler


class SaveController:

    @staticmethod
    def save(request: Request):
        """
        Method used to save pass game info to save handler
        """
        filename = request.inputs['filename']
        SaveHandler.add_file_path(filename)
        save_handler = SaveHandler()
        save_handler.save({"player": request.inputs['ext'][1], "tamagotchis": request.inputs['ext'][0],
                           "game_duration": request.inputs['ext'][2]})
        exit(0)

import json
from pathlib import Path

from Player import Player


class GameSaver:
    def __init__(self, file_to_save: str) -> None:
        self.file_to_save = Path(file_to_save)
        self.save_data = None

    def save(self, **kwargs: dict | object | list) -> str:
        self.save_data = json.dumps(kwargs)
        return self.save_data

    def load(self, *args) -> tuple:
        player = None
        if self.save_data is not None:
            data = json.loads(self.save_data)
            if len(args) > 1:
                return tuple(data[key] for key in args)
            elif len(args) == 1:
                return data[args[0]]
            else:
                for key in data.keys():
                    if key == "player":
                        player_param = []
                        for i in range(len(data[key].keys())):
                            player_param.append(data[key][list(data[key].keys())[i]])
                        player = Player(name=player_param[0], biscuit=player_param[1])
                        del data["player"]
                        break
                return tuple(data[key] for key in data.keys()) + (player,)
        else:
            pass

    def save_to_file(self) -> None:
        with open(self.file_to_save, "w") as file:
            if self.save_data is not None:
                file.write(self.save_data)

    def load_to_file(self) -> tuple:
        with open(self.file_to_save, "r") as file:
            self.save_data = file.read()
        return self.load()

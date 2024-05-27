import json
import os.path

from pathlib import Path

import tamagoatchi


class SaveHandler:
    """
    Class used to handle save in file
    """

    """
    Save Dir location
    """
    save_dir = os.path.join(os.path.dirname(tamagoatchi.__file__), "saves")
    """
    path of save_file 
    """
    file_path: Path

    def __init__(self) -> None:
        """
        init save path
        """
        self.path = SaveHandler.file_path

    def save(self, data: dict) -> None:
        """
        Write data in save file
        """
        try:
            with open(self.path, 'w') as file:
                file.write(json.dumps(data))
        except ValueError:
            tamagoatchi.logger.error("Failed to saved datas")

    def load(self) -> dict:
        """
        load data from save file
        """
        try:
            with open(self.path, 'r') as file:
                return json.loads(file.read())
        except ValueError:
            tamagoatchi.logger.error('Failed to load data')

    @classmethod
    def add_file_path(cls, file_path: str):
        """
        Add file save path in save_dir
        """
        if file_path is not None:
            cls.file_path = Path(cls.save_dir, f"{file_path}" + ".json").resolve()

import json
import os.path

from pathlib import Path

import tamagoatchi


class SaveHandler:
    save_dir = os.path.dirname(tamagoatchi.__file__) + "\\saves"
    file_path: Path

    def __init__(self) -> None:
        self.path = SaveHandler.file_path

    def save(self, data: dict) -> None:
        try:
            with open(self.path, 'w') as file:
                file.write(json.dumps(data))
        except ValueError:
            tamagoatchi.logger.error("Failed to saved datas")

    def load(self) -> dict:
        try:
            with open(self.path, 'r') as file:
                return json.loads(file.read())
        except ValueError:
            tamagoatchi.logger.error('Failed to load data')

    @classmethod
    def add_file_path(cls, file_path: str):
        if file_path is not None:
            cls.file_path = Path(cls.save_dir + f"\\{file_path}" + ".json").resolve()

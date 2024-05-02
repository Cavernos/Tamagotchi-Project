from pathlib import Path

class GameSaver:
    def __init__(self, file_to_save: Path = Path("")) -> None:
        self.file_to_save = file_to_save
        self.save_data = None
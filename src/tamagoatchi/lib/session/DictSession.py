class DictSession:
    def __init__(self):
        self.session = {}

    def get(self, key, default=None):
        if key in self.session:
            return self.session[key]
        return default

    def set(self, key, value) -> None:
        self.session[key] = value

    def delete(self, key) -> None:
        del self.session[key]

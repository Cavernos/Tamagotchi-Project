class Request:
    def __init__(self, json: dict):
        self.json = json
        self.inputs = json['inputs'] if 'inputs' in json else None

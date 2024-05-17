class Request:
    """
    A class used to materialize a request

    Attributes
    ----------
    json: dict
    headers of the request
    """
    def __init__(self, json: dict):
        self.json = json
        self.inputs = json['inputs'] if 'inputs' in json else None

import string
from typing import Any

from app.definitions import ROOT_DIR


class SuperFormatter(string.Formatter):
    def __init__(self, default='') -> None:
        self.default = default

    def get_value(self, key, args, kwds) -> Any:
        if isinstance(key, str):
            return kwds.get(key, self.default.format(key))
        else:
            return string.Formatter.get_value(key, args, kwds)

    def format_field(self, value, spec: str) -> Any:
        if spec == 'call':
            return value()
        if spec.startswith('repeat'):
            split_arr = spec.partition(':')
            it = split_arr[0].split()[2]
            template = split_arr[-1]
            return '\n'.join(
                [self.format(template, **{it: val}, i=i + 1) for i, val in zip(range(0, len(value)), value)])
        else:
            return super(SuperFormatter, self).format_field(value, spec)


class View:
    def __init__(self, path: str, objects, ext_dict: dict) -> None:
        self.path = path
        self.qualified_path_name = ROOT_DIR + '\\views\\' + path + '.txt'
        self.inputs = {}
        self.objects = objects
        with open(self.qualified_path_name, 'r') as file:
            self.header = ext_dir
            self.__content = file.read()
            self.compile()
            self.parse(objects)

    def compile(self) -> None:
        open_brackets = 0





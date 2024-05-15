from abc import ABC


class Model(ABC):
    @classmethod
    def get_instance(cls, attr_dict: dict):
        obj = cls.__new__(cls)
        for key, value in attr_dict.items():
            obj.__setattr__(key, value)
        return obj

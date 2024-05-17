from abc import ABC


class Model(ABC):
    """
    Class used to define all models classes
    """
    @classmethod
    def get_instance(cls, attr_dict: dict):
        """
        Function to get instance from dict
        """
        obj = cls.__new__(cls)
        for key, value in attr_dict.items():
            obj.__setattr__(key, value)
        return obj

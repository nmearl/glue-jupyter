from glue.config import DictRegistry
import re
from functools import wraps


def convert(name):
    """
    Converts camel case strings to snake case.

    Returns
    -------
    : str
        Name converted to snake case.
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)

    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


class ViewerRegistry(DictRegistry):
    def __init__(self):
        super().__init__()

    def add(self, name, cls):
        if name in self.members:
            raise ValueError(f"Viewer with the name {name} already exists, "
                             f"please choose a different name.")
        else:
            self.members[name] = cls

    def __call__(self, name=None):
        def decorator(cls, key):
            if key is None:
                key = convert(cls.__name__)

            @wraps(cls)
            def cls_wrapper():

                self.add(key, cls)

            return cls_wrapper
        return lambda x: decorator(x, name)


class ComponentRegistry(DictRegistry):
    def __init__(self):
        super().__init__()

    def add(self, name, cls):
        if name in self.members:
            raise ValueError(f"Viewer with the name {name} already exists, "
                             f"please choose a different name.")
        else:
            self.members[name] = cls

    def __call__(self, name=None):
        def decorator(cls, key):
            if key is None:
                key = convert(cls.__name__)

            @wraps(cls)
            def cls_wrapper():

                self.add(key, cls)

            return cls_wrapper
        return lambda x: decorator(x, name)


viewers = ViewerRegistry()

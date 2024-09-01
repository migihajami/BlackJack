from abc import ABC, abstractmethod


class Savable(ABC):

    @abstractmethod
    def save_state(self):
        pass


def save_post_state(f):
    def wrapper(*args):
        result = f(args)
        instance: Savable = args[0]
        instance.save_state()
        return result
    return wrapper

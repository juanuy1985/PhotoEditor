from abc import ABCMeta, abstractmethod

class Reader:
    __metaclass__ = ABCMeta

    @classmethod
    def load(self, path): raise NotImplementedError


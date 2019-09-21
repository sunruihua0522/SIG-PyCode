
from abc import ABCMeta, abstractmethod

class IMotion:
    __metaclass__ = ABCMeta

    def __init__(self,name):
        self.Name = name

    @abstractmethod
    def Run(self):
        pass

    @abstractmethod
    def GetOil(self,*args):
        pass

    @abstractmethod
    def GetInfo(self):
        pass
from abc import ABCMeta, abstractmethod
import copy
from time import sleep


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self, other):
        pass

class Class1(Prototype):
    data1 = None
    data2 = None
    data3 = None

    def download_data1(self):
        sleep(1)
        self.data1 = 126
    def download_data2(self):
        sleep(1)
        self.data2 = 127
    def download_data3(self):
        sleep(1)
        self.data3 = 128

    def clone(self):
        newobj = type(self)()
        newobj.data1 = copy.deepcopy(self.data1)
        newobj.data2 = copy.deepcopy(self.data2)
        newobj.data3 = copy.deepcopy(self.data3)
        return newobj
    
    def __str__(self):
        return "data1={}, data2={}, data3={}".format(self.data1, self.data2, self.data3)

o1 = Class1()
o1.download_data1()
o1.download_data2()
o1.download_data3()
print(o1)
o2 = o1.clone()
print(o2)


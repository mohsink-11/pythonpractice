from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def makePayment(self,amount):
        pass
        ...


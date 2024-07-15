from abc import ABC

class Device(ABC):
    
    def __init__(self) -> None:
        self.__status = 'off'
        self.type = None

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status in ['on', 'off']:
            self.__status = status
        
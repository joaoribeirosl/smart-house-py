from functools import reduce
from device_factory import DeviceFactory

class SmartHouse:
    __instance = None
    __is_initialized = None

    @staticmethod
    def get_instance():
        if not SmartHouse.__instance:
            SmartHouse.__instance = SmartHouse()
        return SmartHouse.__instance
    
    def __init__(self) -> None:
        if SmartHouse.__is_initialized:     
            raise Exception('this class must have only one instance, if you dont like it please, remove C:\Windows\System32')
        SmartHouse.__is_initialized = True
        self.devices = []
        self.__observers = []
        self.__limit = 0

    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, value):
        self.__limit = value
        
    def add(self, observer):
        self.__observers.append(observer)
        
    def remove(self, observer):
        self.__observers.remove(observer)

    def add_device(self, type):
        if len(self.devices) < self.__limit:
            device = DeviceFactory.create_device(type)
            self.devices.append(device)
            self.notify(device)
        else:
            print(f'you cannot add this {type}, you reached the device limit {self.limit}')

    def remove_device(self, id):
        if id < len(self.devices):
            removed_device = self.devices.pop(id)
            self.notify_remove(removed_device)
        else:
            print('Device not found')
        
    def get_all_device_status(self):     
        return [[device.type, device.status] for device in self.devices]
    
    def get_all_devices(self):     
        return [(i, device.type) for i, device in enumerate(self.devices)]
    
    def turn_off_all_light(self):
        return list(map(self.turn_off_light, self.devices))

    def turn_off_light(self, device):
        if device.type == 'light':
            if device.status == 'on':
                device.status = 'off'
                device.trigger('turn_off')

    
    def turn_on_all_lights(self):
        return list(map(self.turn_on_light, self.devices))

    def turn_on_light(self, device):
        if device.type == 'light':
            if device.status == 'off':
                device.status = 'on'
                device.trigger('turn_on')
 
    def get_all_on_devices(self):
        on_devices = list(filter(self.get_on_devices, self.devices))
        return [device.type for device in on_devices]
    
    def get_on_devices(self, device):
        return device.status == 'on'
        
    def count_all_on_devices(self):
        return reduce(lambda count, device: count + 1 if device.status == 'on' else count, self.devices, 0)

    def notify(self, device):
        for observer in self.__observers:
            observer.update(device)

    def notify_remove(self, device):
        for observer in self.__observers:
            observer.update_remove(device)
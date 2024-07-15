from light import Light
from security_system import SecuritySystem
from thermostat import Thermostat
from abc import abstractmethod


class DeviceFactory:
    
    @abstractmethod
    def create_device(device_type):
        device_type = device_type.strip().lower()
        if device_type == 'light':
            return Light()
        elif device_type == 'thermostat':
            return Thermostat()
        elif device_type == 'security_system':
            return SecuritySystem()
        else:
            raise ValueError('not found')

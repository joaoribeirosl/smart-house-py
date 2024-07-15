from device import Device
from transitions import Machine
from enum import Enum

class ThermostatStates(Enum):
    OFF = 1
    HEATING = 2
    COOLING = 3

class Thermostat(Device):

    def __init__(self) -> None:
        super().__init__()
        self.type = 'thermostat'
        self.thermostat_state_machine = Machine(model = self, states = ThermostatStates, initial = ThermostatStates.OFF)  

        self.thermostat_state_machine.add_transition(
            trigger = 'heat',
            source = ThermostatStates.OFF,
            dest = ThermostatStates.HEATING,      
        )

        self.thermostat_state_machine.add_transition(
            trigger = 'cool',
            source = ThermostatStates.HEATING,
            dest = ThermostatStates.COOLING,   
        )

        self.thermostat_state_machine.add_transition(
            trigger = 'turn_off',
            source = ThermostatStates.COOLING,
            dest = ThermostatStates.OFF    
        )   
    
    def turn_on(self):
        self.status = 'on'
        self.trigger('heat')

    def turn_off(self):
        self.status = 'off'
        self.trigger('turn_off')
        


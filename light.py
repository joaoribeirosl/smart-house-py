from device import Device
from transitions import Machine
from enum import Enum

class LightStates(Enum):
    ON = 1
    OFF = 2

class Light(Device):
    
    def __init__(self) -> None:
        super().__init__()
        self.type = 'light'
        self.light_state_machine = Machine(model = self, states = LightStates, initial = LightStates.OFF)  

        self.light_state_machine.add_transition(
            trigger = 'turn_on',
            source = LightStates.OFF,
            dest = LightStates.ON,
        )

        self.light_state_machine.add_transition(
            trigger = 'turn_off',
            source = LightStates.ON,
            dest = LightStates.OFF,    
        )

    def turn_on(self):
        self.status = 'on'
        self.trigger('turn_on')

    def turn_off(self):
        self.status = 'off'
        self.trigger('turn_off')

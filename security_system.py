from device import Device
from transitions import Machine
from enum import Enum

class SecuritySystemStates(Enum):
    UNARMED = 1
    ARMED_WITH_PEOPLE_IN_HOME = 2
    ARMED_WITHOUT_PEOPLE_IN_HOME = 3

class SecuritySystem(Device):
    def __init__(self) -> None:
        super().__init__()
        self.type = 'security_system'
        self.security_system_state_machine = Machine(model = self, states = SecuritySystemStates, initial = SecuritySystemStates.UNARMED)  

        self.security_system_state_machine.add_transition(
            trigger = 'arm_with_people_in_home',
            source = SecuritySystemStates.UNARMED,
            dest = SecuritySystemStates.ARMED_WITH_PEOPLE_IN_HOME,  
        )

        self.security_system_state_machine.add_transition(
            trigger = 'arm_without_people_in_home',
            source = SecuritySystemStates.ARMED_WITH_PEOPLE_IN_HOME,
            dest = SecuritySystemStates.ARMED_WITHOUT_PEOPLE_IN_HOME    
        )

        self.security_system_state_machine.add_transition(
            trigger = 'unarm',
            source = SecuritySystemStates.ARMED_WITHOUT_PEOPLE_IN_HOME,
            dest = SecuritySystemStates.UNARMED    
        )   

    def turn_on(self):
        self.status = 'on'
        self.trigger('arm_with_people_in_home')

    def turn_off(self):
        self.status = 'off'
        self.trigger('unarm')
import sys
from light import Light
from observer import Observer
from security_system import SecuritySystem
from smart_house import SmartHouse
from thermostat import Thermostat 

def help():
    print('''
          
        usage: python main.py [<set_limit>]
        Options:    
        set_limit <limit>           : set a limit to devices in the smart house 
          
          ''')
    
def menu():
    print('''
                      <<< Menu >>>
          
        [1] status                      : verify device status
        [2] control <device>            : control a specific device
        [3] add <device>                : add a new device  
        [4] remove <device>             : remove an existing device
        [5] misc                        : miscellaneous info about an existing device
        [0] exit                        : exit from application
          ''')
    
def device_menu():
    print('''
                      <<< Device Menu >>>
          
        [1] light                      
        [2] thermostat
        [3] security system   
        [0] back             
          ''')
def light_menu():
    print('''
                      <<< Light Menu >>>
          
        [1] turn on                      
        [2] turn off              
          ''')
    
def thermostat_menu():
    print('''
                      <<< Thermostat Menu >>>
          
        [1] heat                      
        [2] cool              
        [3] turn off              
          ''')
    
def security_system_menu():
    print('''
                      <<< Security System Menu >>>
          
        [1] arm_with_people_in_home                      
        [2] arm_without_people_in_home              
        [3] unarm             
          ''')
    
def misc_menu():
    print('''
                      <<< Misc Menu >>>
          
        [1] get all on devices                    
        [2] count all on devices
        [0] back              
                  
          ''')
    
    
def main():
    if len(sys.argv) < 2:
        help()
        return
    
    sh = SmartHouse.get_instance()
    observer = Observer()
    sh.add(observer)

    command = sys.argv[1]
    
    if command == 'set_limit':
        sh.limit = int(sys.argv[2]) 
    else:
        print()
        print(f'`{command}` is not recognized as an internal or external command, operable program or batch file.')
        help()
        return
    
    in_menu = True
    while in_menu:
        menu()
        op = input('select an option: ')

        if op == '1':
            print(sh.get_all_device_status())

        elif op == '2':
            if len(sh.devices):
                print(sh.get_all_devices())
                print()
                id = int(input('which device you want to handle? ')) 

                actual_device = sh.devices[id]   
        
                if isinstance(actual_device, Light):
                    
                    # if actual_light.status == 'off':
                    all_lights_input = input(f"do you want turn 'on' if'  all lights? (y/n) '").strip().lower()
                    if all_lights_input == 'y':
                        sh.turn_on_all_lights()
                    else:    
                        light_menu()
                        light_input = input('select an option: ')

                        if light_input == '1':
                            if actual_device.status == 'off':
                                actual_device.turn_on()
                        else:
                            if actual_device.status == 'on':
                                actual_device.turn_off()

                elif isinstance(actual_device, Thermostat):
                    thermostat_menu()
                    thermostat_input = input('select an option: ')

                    if thermostat_input == '1':
                        if actual_device.status != 'heat':
                            actual_device.turn_on()
                    elif thermostat_input == '2':
                        if actual_device.status != 'cool':
                            actual_device.cool()
                    else: 
                        if actual_device.status != 'off':
                            actual_device.turn_off()
   
                elif isinstance(actual_device, SecuritySystem):
                    security_system_menu()
                    security_system_input = input('select an option: ')
                  
                    if security_system_input == '1':
                        if actual_device.status != 'arm_with_people_in_home':
                            actual_device.turn_on()
                    elif security_system_input == '2':
                        if actual_device.status != 'arm_without_people_in_home':
                            actual_device.arm_without_people_in_home()
                    else: 
                        if actual_device.status != 'off':
                            actual_device.turn_off()
            
        elif op == '3':
            in_menu_device = True
            while in_menu_device:
                device_menu()
                op_device = input('select an option: ')

                if op_device == '1':
                    sh.add_device('light')
                elif op_device == '2':
                    sh.add_device('thermostat')
                elif op_device == '3':
                    sh.add_device('security_system')
                elif op_device == '0':
                    in_menu_device = False
                else:
                    print('invalid option')
        
        elif op == '4':
            if len(sh.devices):
                print(sh.get_all_devices())
                print()
                id = int(input('which device you want to remove? [put the device_id here] '))
                sh.remove_device(id)

        elif op == '5':
            in_misc_menu = True
            while in_misc_menu:
                misc_menu()
                op_device = input('select an option: ')

                if op_device == '1':
                    print(sh.get_all_on_devices())
                elif op_device == '2':
                    print(f"{sh.count_all_on_devices()} {'device is' if sh.count_all_on_devices() == 1 else 'devices are'} turned on")
                else: 
                    in_misc_menu = False

        elif op == '0':
            in_menu = False

        else: 
            print('invalid option')

if __name__ == '__main__':
    main()
  